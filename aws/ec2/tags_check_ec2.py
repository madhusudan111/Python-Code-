import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances(InstanceIds=[])
for instance in response['Reservations'][0]['Instances']:
    id = instance['InstanceId']
    #print (instance['Tags'])
    tag_list = []
    for tag_key in instance['Tags']:
        tag_list.append(tag_key['Key'])
    #print (tag_list)
    if 'Application' not in tag_list:
        stop_response = ec2.stop_instances(InstanceIds=[id])
        while True:
            ec2_response = ec2.describe_instances(InstanceIds=[id])
            ec2_state = ec2_response['Reservations'][0]['Instances'][0]['State']['Name']
            if ec2_state == 'stopped':
                print ("EC2 ID  {} stopped".format(id))
                break
            else:
                continue
    else:
        print ("Application Tag is found for the EC2: {}".format(id))