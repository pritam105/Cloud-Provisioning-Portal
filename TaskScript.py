import sys
import boto3
from botocore.exceptions import ClientError

def StartInstance(sid) :
    instance_ids = sid
    
    ec2 = boto3.client('ec2')

    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=instance_ids, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=instance_ids, DryRun=False)
        print(response)
    except ClientError as e:
        print(e)


def StopInstance(sid):
    ec2 = boto3.resource('ec2')

    #instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    all_instance_ids = sid


    ec2_stop = boto3.client('ec2')
    ec2_stop.stop_instances(InstanceIds=all_instance_ids)

#StopInstance(['i-054dceae0fb8859d3', 'i-0c070cc0650e84d66'])
#StartInstance(['i-054dceae0fb8859d3', 'i-0c070cc0650e84d66'])
