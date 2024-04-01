# reboot EC2 Instance
# You can improve the code to get the Instance List using describe_instance() and loop through. 
#import Modules
import boto3
#reboot Logic
#Functions
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    #variables
    instance_id = [ "i-0239a102339645651", "i-079aa95a6315965bb" ]
    for id in instance_id:
        response = ec2.reboot_instances(InstanceIds=[id,],DryRun=False)
        responsecode = response['ResponseMetadata']['HTTPStatusCode']
        if responsecode == 200:
            print ("Instance ID: {} is rebooted".format(id))
            print ("\n")
        else:
            print ("Instance ID: {} failed to reboot".format(id))
