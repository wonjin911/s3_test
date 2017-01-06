import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('test.txt', 'rt')
s3.Bucket('wonjin-test').put_object(Key='test.txt', Body=data)
