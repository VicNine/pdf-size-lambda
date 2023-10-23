def lambda_handler(event, context):
    print("test")
    return {
        'statusCode': 200,
        'body': "test"
    }