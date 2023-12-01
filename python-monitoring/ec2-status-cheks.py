import boto3
import schedule

ec2_client = boto3.client('ec2', region_name = "us-east-2")
ec2_resource = boto3.resource('ec2', region_name = "us-east-2")

# reservations = ec2_client.describe_instances()

# for reservation in reservations['Reservations']:
#     instances = reservation['Instances']
#     for instance in instances:
#         print(f"Instance {instance['InstanceId']} is '{instance['State']['Name']}' state")


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances = True
    )

    for status in statuses['InstanceStatuses']:
        instance_state = status['InstanceState']['Name']
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        print(f"Instance {status['InstanceId']} state is '{instance_state}' with instance status '{instance_status}' and system status is '{system_status}'")
    
    print("=====================================================")

schedule.every(10).seconds.do(check_instance_status)

while True:
    schedule.run_pending()