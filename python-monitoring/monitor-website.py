import requests
import smtplib
import os
import paramiko
import boto3
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
SUPPORT_EMAIL = os.environ.get('SUPPORT_EMAIL')

def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject:[URGENT] SITE DOWN!!!\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, SUPPORT_EMAIL, message)

def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='18.118.156.17', username='ec2-user', key_filename='C:\\DevOps\\Nana\\AWS\\devops-nana-key.pem')
    stdin, stdout, stderr = ssh.exec_command('docker start e56930ec2c1b')
    print(stdout.readlines())
    ssh.close()

def restart_server_and_container():
    # restart server
    print('Rebooting the server...')
    ec2_client = boto3.client('ec2', region_name = "us-east-2")
    instance_id = "i-0e34a3cc91338541d"
    response = ec2_client.reboot_instances(InstanceIds=[instance_id])
    
    # restart the application
    while True:
        statuses = ec2_client.describe_instance_status(InstanceIds=[instance_id])
        for status in statuses['InstanceStatuses']:
            instance_state = status['InstanceState']['Name']
            if instance_state == 'running':
                time.sleep(10)
                restart_container()
                break

def monitor_application():
    try:
        response = requests.get('http://ec2-18-118-156-17.us-east-2.compute.amazonaws.com:80')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application is down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as e:
        print(f'Connection error happened: {e}')
        msg = 'Application not accessible at all'
        send_notification(msg)

schedule.every(10).minutes.do(monitor_application)

while True:
    schedule.run_pending()
