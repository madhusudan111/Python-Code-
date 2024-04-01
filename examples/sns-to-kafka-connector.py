#!/usr/bin/env python3
import json
import boto3
import kafka
from kafka import KafkaProducer
security_protocol = "SASL_SSL"
sasl_mechanism = "SCRAM-SHA-512"
topic = "perftesting"
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:256867920320:cpu-alerts:9db69000-6ffd-416b-95fc-ff7b5fbcb768', 'Sns': {'Type': 'Notification', 'MessageId': '38215f29-2ef3-5368-8518-046bc249b66b', 'TopicArn': 'arn:aws:sns:us-east-1:256867920320:cpu-alerts', 'Subject': 'ALARM: "cpu-alarm" in US East (N. Virginia)', 'Message': '{"AlarmName":"cpu-alarm","AlarmDescription":null,"AWSAccountId":"256867920320","AlarmConfigurationUpdatedTimestamp":"2022-07-09T02:36:47.890+0000","NewStateValue":"ALARM","NewStateReason":"Threshold Crossed: 1 out of the last 1 datapoints [99.83274983791787 (09/07/22 02:34:00)] was greater than the threshold (80.0) (minimum 1 datapoint for OK -> ALARM transition).","StateChangeTime":"2022-07-09T02:39:54.536+0000","Region":"US East (N. Virginia)","AlarmArn":"arn:aws:cloudwatch:us-east-1:256867920320:alarm:cpu-alarm","OldStateValue":"INSUFFICIENT_DATA","OKActions":[],"AlarmActions":["arn:aws:sns:us-east-1:256867920320:cpu-alerts"],"InsufficientDataActions":[],"Trigger":{"MetricName":"CPUUtilization","Namespace":"AWS/EC2","StatisticType":"Statistic","Statistic":"AVERAGE","Unit":null,"Dimensions":[{"value":"i-0d2ef44803a38dbc6","name":"InstanceId"}],"Period":60,"EvaluationPeriods":1,"DatapointsToAlarm":1,"ComparisonOperator":"GreaterThanThreshold","Threshold":80.0,"TreatMissingData":"missing","EvaluateLowSampleCountPercentile":""}}', 'Timestamp': '2022-07-09T02:39:54.584Z', 'SignatureVersion': '1', 'Signature': 'rC3TYqzLHs9V/4BOpZm1IRlER/Ckk00LIcrZeATHCjaxKCJ09wbmAuo6tI398RnR+BD57mrh7kjKew06jOVy3ZMiAKnAKL088D5FI+JB2WwgL69SRsWjevpFu1sYCvntyFz2DXdCawx3/u9Xe80WrEY9mANRmakC1Uysh36y/yIoqGebDM/LLe8G8UQk+9azSu3u3+xgzMeZxWOLkYrUyfqq4T3CgbBzleg5ZcuLiT1z2kU5hemUObbfrpaG0BKXMai/c9c2zZyDAkVSmaoyWzfaDaoYhSw3nn2n/i6wVPhqQPTPM2sk5lYjA2UmZFOi2wOp5sc9q7jwtXDGMCQhXQ==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:256867920320:cpu-alerts:9db69000-6ffd-416b-95fc-ff7b5fbcb768', 'MessageAttributes': {}}}]}
def event_procesor(event):
    awsAccountId = json.loads(event['Records'][0]['Sns']['Message'])['AWSAccountId']
    metricName = json.loads(event['Records'][0]['Sns']['Message'])['Trigger']['MetricName']
    instanceId = json.loads(event['Records'][0]['Sns']['Message'])['Trigger']['Dimensions'][0]['value']
    message = {}
    message.update({'awsAccountId':awsAccountId,'metricName':metricName,'instanceId':instanceId})
    msg = bytes(str(message),'utf-8')
    return msg
def get_secrets():
    # Get Secrets
    secret_name = "AmazonMSK_dev/admin"
    region_name = "us-east-1"
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name )
    secret = client.get_secret_value(SecretId=secret_name)
    return secret
def publish(msg, username, password):
    servers = "b-2.edwiki.htga4a.c23.kafka.us-east-1.amazonaws.com:9096,b-1.edwiki.htga4a.c23.kafka.us-east-1.amazonaws.com:9096,b-3.edwiki.htga4a.c23.kafka.us-east-1.amazonaws.com:9096"
    producer = KafkaProducer(bootstrap_servers=servers,security_protocol=security_protocol,sasl_mechanism=sasl_mechanism,sasl_plain_username=username,sasl_plain_password=password)
    response  = producer.send(topic,msg)
    print (response.get(timeout=60))
    producer.close()
msg = event_procesor(event)
secret = get_secrets()
username = json.loads(secret['SecretString'])['username']
password = json.loads(secret['SecretString'])['password']
publish(msg, username, password)
