import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

print("List of S3 Buckets:")
for bucket in response['Buckets']:
    print(bucket['Name'])

# Testing GitHub Actions trigger
