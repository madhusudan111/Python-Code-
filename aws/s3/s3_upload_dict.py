# How to import modules
import boto3
# String data Types
file = "access.log"

# Dictionary Type
buckets = { "bucket1": "dpt3-web-data-01", "bucket2": "dpt3-web-data-02" }
# How to create client for S3 service
s3 = boto3.resource('s3')
# Parsing the data
#Data Processing
s3.meta.client.upload_file(file, buckets['bucket1'], 'data/access.log')
#File "access.log" uploaded successfully to Bucket:dpt3-web-data-01
print ("File {} uploaded successfully to Bucket: {}".format(file, buckets['bucket1']))
s3.meta.client.upload_file(file, buckets['bucket2'], 'data/access.log')
print ("File {} uploaded successfully to Bucket: {}".format(file, buckets['bucket2']))
