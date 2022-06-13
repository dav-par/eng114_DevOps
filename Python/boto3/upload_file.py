import boto3
# Create an S3 access object
s3 = boto3.client('s3')


s3.upload_file(
Filename = 'test.txt',
Bucket = 'eng114-david-bucket',
Key = 'test1.txt'
)