import base64
import boto3
import os
import json
import uuid
import time

def lambda_handler(event, context):
    # get base64 encoded file content from event
    body = json.loads(event['body'])

    # get base64 encoded file content from event
    base64_file_content = body['file_content_base64']
    if not base64_file_content:
        print(base64_file_content)
        return {
            'statusCode': 400,
            'body': 'invaild file_content_base64'
        }
    # decode base64 encoded file content
    file_content = base64.b64decode(base64_file_content)
    # calculate file size in megabytes
    file_size_in_bytes = len(file_content)
    file_size_in_megabytes = file_size_in_bytes / (1024 * 1024)

    # store file in S3 bucket
    bucket_name = os.environ['BUCKET_NAME']
    s3 = boto3.client('s3')
    # gen file name
    file_name = body['file_name']
    unique_id = str(uuid.uuid4())
    timestamp = int(time.time())
    file_name = f"{file_name}_{unique_id}_{timestamp}"

    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content, ContentType='application/pdf')
        print(f'Successfully uploaded {file_name} to {bucket_name}.')
    except Exception as e:
        print(f'Error uploading {file_name} to {bucket_name}: {e}')
        return {
            'statusCode': 500,
            'body': 'File upload failed'
        }
    return {
        'statusCode': 200,
        'body': f'File size: {file_size_in_megabytes:.2f} MB'
    }
