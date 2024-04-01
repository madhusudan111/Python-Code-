import boto3
ec2_resource = boto3.resource('ec2') 
ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups()
def check_rules():
    for sg_list in response['SecurityGroups']:
        sg_id = sg_list['GroupId']
        sg = ec2_resource.SecurityGroup(sg_id)
        rules = sg.ip_permissions
        for rule in rules:
            for sourcerange in rule['IpRanges']:
                if sourcerange['CidrIp'] == '0.0.0.0/0':
                    sg.revoke_ingress(IpPermissions=[rule])
                    print ("DELETED: Security Group ID:  {} Rule:  {}".format(sg.group_id, rule))
                else:
                    print ("Rules are as per standards")
check_rules()