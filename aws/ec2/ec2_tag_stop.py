# Stop EC2 servers having Name tag as webserver
import boto3
ec2 = boto3.client('ec2',region_name="us-east-1")
# Data Input
ec2_list = ec2.describe_instances(InstanceIds=[])
instance_ids = []
for instance_list in ec2_list['Reservations'][0]['Instances']:
    for tags_list in  instance_list['Tags']:
        #print (tags_list)
        if tags_list['Key'] == "Name":
                if tags_list['Value'] == "webserver":
                    if instance_list['State']['Name'] == "stopped":
                        print ("Instance {} is already stopped".format(instance_list['InstanceId']))
                    else:
                        instance_ids.append(instance_list['InstanceId'])
# Business Logic
def stop(instance_ids):
    for instance_id in instance_ids:
        ec2.stop_instances(InstanceIds=[instance_id])
        while True:
            instance_meta = ec2.describe_instances(InstanceIds=[instance_id])
            state = instance_meta['Reservations'][0]['Instances'][0]['State']['Name']
            if state == "stopped":
                print ("Instance ID: {} is now stopped".format(instance_id))
                break
stop(instance_ids)