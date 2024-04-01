# reboot EC2 Instance
#import Modules
import boto3
#Importing EC2 Methods
ec2 = boto3.client('ec2')
#variables
instance_id = [ "i-0bf50d5597990a179", "i-0b75d69033a547c00" ]

#reboot Logic
#Functions
def reboot(instance_id):
    for id in instance_id:
        response = ec2.reboot_instances(InstanceIds=[id,],DryRun=False)
        responsecode = response['ResponseMetadata']['HTTPStatusCode']
        if responsecode == 200:
            print ("Instance ID: {} is rebooted".format(id))
            print ("\n")
        else:
            print ("Instance ID: {} failed to reboot".format(id))
reboot(instance_id)
