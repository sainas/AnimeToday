import boto3
import time

s3 = boto3.client('s3')
s3.create_bucket(Bucket=time.strftime("%Y-%m-%d", time.localtime()))
