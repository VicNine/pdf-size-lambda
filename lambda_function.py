import base64

def lambda_handler(event, context):
    # get base64 encoded file content from event
    base64_file_content = event['body']
    if not base64_file_content:
        return {
            'statusCode': 400,
            'body': 'No file provided'
        }
    
    # decode base64 encoded file content
    file_content = base64.b64decode(base64_file_content)
    
    # calculate file size in megabytes
    file_size_in_bytes = len(file_content)
    file_size_in_megabytes = file_size_in_bytes / (1024 * 1024)
    
    return {
        'statusCode': 200,
        'body': f'File size: {file_size_in_megabytes:.2f} MB'
    }
