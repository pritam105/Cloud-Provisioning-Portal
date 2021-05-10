import sys
import boto3
from botocore.exceptions import ClientError

def StartInstance(sid) :
    instance_id = sid
    
    ec2 = boto3.client('ec2')

    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)


def StopInstance():
    ec2 = boto3.resource('ec2')

    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    all_instance_ids = []

    for instance in instances:
        all_instance_ids.append(instance.id)


    ec2_stop = boto3.client('ec2')
    ec2_stop.stop_instances(InstanceIds=all_instance_ids)

