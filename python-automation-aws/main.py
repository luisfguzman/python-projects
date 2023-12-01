import boto3

ec2_client = boto3.client('ec2', region_name = "us-west-1")
ec2_resource = boto3.resource('ec2', region_name = "us-west-1")

new_vpc = ec2_resource.create_vpc(
    CidrBlock = "10.0.0.0/16"
)

new_vpc.create_subnet(
    CidrBlock = "10.0.1.0/24"
)

new_vpc.create_subnet(
    CidrBlock = "10.0.2.0/24"
)

new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc-boto3'
        },
    ]
)

all_vpcs = ec2_client.describe_vpcs()
loop_vpcs = all_vpcs["Vpcs"]

for vpc in loop_vpcs:
    print(f"VPC ID: {vpc["VpcId"]}")

    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(f"Cidr Block State: {assoc_set["CidrBlockState"]["State"]}\n")
