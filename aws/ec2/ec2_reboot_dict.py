# reboot EC2 Instance
#import Modules
import boto3
#Importing EC2 Methods
ec2 = boto3.client('ec2')
#variables
instance_id = {'id1': 'i-0bf50d5597990a179', 'id2': 'i-0b75d69033a547c00'}

#reboot Logic
#Functions
def reboot(id):
    response = ec2.reboot_instances(InstanceIds=[id,],DryRun=False)
    print ("Reboot response is: {}".format(response))
    print ("Instance ID: {} is rebooted".format(id))
    print ("\n")
reboot(instance_id['id1'])
reboot(instance_id['id2'])
