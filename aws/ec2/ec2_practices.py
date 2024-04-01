## Scenario -1  List Instance Ids
import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
for instance in instances['Reservations'][0]['Instances']:
    print (instance['InstanceId'])
## Scenario -2 List Name Tag of EC2 Instances
import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
for instance in instances['Reservations'][0]['Instances']:
    InstanceId = instance['InstanceId']
    for tags in instance['Tags']:
        if tags['Key'] == "Name":
            value = tags['Value']
            print ("Instance Id: {} and Tag Name: {}".format(InstanceId, value))
