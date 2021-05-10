from celery import shared_task
from .models import *
import boto3

@shared_task
def task1() :
    ec2 = boto3.resource('ec2')

    # create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-00b6a8a2bd28daf19',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',

        #KeyName='FirstEC2'
    )