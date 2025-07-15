import boto3

def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name,  CreateBucketConfiguration = {'LocationConstraint': 'us-west-2'})
    print(f"Bucket {bucket_name} created.")

def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted.")

if __name__ == "__main__":
    bucket_name = "my-test-bucket-" + str(hash("farvez"))
    create_bucket(bucket_name)
    delete_bucket(bucket_name)
