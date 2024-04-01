# Try - except - logging concepts
import boto3
import logging
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.INFO, filename="error.log")
ec2_resource = boto3.resource('ec2') 
ec2_client = boto3.client('ec2')
sns = boto3.client('sns')
response = ec2_client.describe_security_groups()
def check_rules():
    try:
        for sg_list in response['SecurityGroups']:
        #sg_id = sg_list['GroupId']
            sg_id = "sg-678899"
            logging.info("Currently working on SG id:{} ".format(sg_id))
            sg = ec2_resource.SecurityGroup(sg_id)
            rules = sg.ip_permissions
            for rule in rules:
                for sourcerange in rule['IpRanges']:
                    if sourcerange['CidrIp'] == '0.0.0.0/0':
                        sg.revoke_ingress(IpPermissions=[rule])
                        print ("DELETED: Security Group ID:  {} Rule:  {}".format(sg.group_id, rule))
                    else:
                        print ("Rules are as per standards")
    except Exception as error:
        logging.error("FAILED: Exception is below")
        print (error)

check_rules()
        

