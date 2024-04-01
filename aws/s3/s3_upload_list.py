# How to import modules
import boto3
# String data Types
file = "access.log"

# List Data type
buckets = [ "dpt3-web-data-01", "dpt3-web-data-02" ]
# How to create client for S3 service
s3 = boto3.resource('s3')
# Parsing the data
#Data Processing
s3.meta.client.upload_file(file, buckets[0], 'data/access.log')
#File "access.log" uploaded successfully to Bucket:dpt3-web-data-01
print ("File {} uploaded successfully to Bucket: {}".format(file, buckets[0]))
s3.meta.client.upload_file(file, buckets[1], 'data/access.log')
print ("File {} uploaded successfully to Bucket: {}".format(file, buckets[1]))
