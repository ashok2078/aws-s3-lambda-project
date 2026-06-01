def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']
    
    print("S3 Triggered 🚀")
    print("Uploaded file:", file_name)

    return {
        'file': file_name
    }
