import boto3
import os
from datetime import datetime

def upload_file_to_s3(file_path, bucket_name, region, access_key_id, secret_access_key):
    # Initialize S3 client
    s3 = boto3.client('s3',
                      region_name=region,
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key)

    # Extract filename from file_path
    file_name = os.path.basename(file_path)

    # Generate unique folder name based on timestamp
    folder_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    # Define the object key by combining the folder name and the file name
    object_key = f'{folder_name}/{file_name}'
    
    url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=3600  # URL expires in 1 hour (you can adjust this as needed)
    )
    print(url)

    # Upload file using the access point
    try:
        response = s3.upload_file(file_path, bucket_name, object_key, ExtraArgs={'ACL': 'bucket-owner-full-control'})
        print("Upload successful")
        return url
    except Exception as e:
        print("Upload failed:", e)

# Usage

