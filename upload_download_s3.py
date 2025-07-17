import boto3

def upload_file(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration = {'LocationConstraint' : 'us-west-2'} )
    print(f"Bucket {bucket_name} is created")
    s3.upload_file('new.txt', bucket_name, 'new.txt')
    print(f"File is uploded succesfully to {bucket_name}")


def download_file(bucket_name):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, 'new.txt', 'new-downloaded.txt')
    print(f"File is downlaoded succesfully to {bucket_name}")

if __name__ == "__main__":
    bucket_name = "farvez-upload" + str(hash('farvez'))

    with open ('new.txt', 'w') as f:
        f.write("uploading by defining the functions")
    
    upload_file(bucket_name)
    download_file(bucket_name)

    


