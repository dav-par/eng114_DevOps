import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

s3.create_bucket(Bucket='eng114-david-bucket', CreateBucketConfiguration={

    'LocationConstraint': 'eu-west-1'})

