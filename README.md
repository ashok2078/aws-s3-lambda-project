#  AWS S3 + Lambda Event-Driven Project

# Project Overview

This project demonstrates a **serverless event-driven architecture** using AWS services.
Whenever a file is uploaded to an S3 bucket, an AWS Lambda function is automatically triggered to process the event.

# Architecture

S3 Bucket → Lambda Function → CloudWatch Logs

# AWS Services Used

* Amazon S3 (Storage & Event Source)
* AWS Lambda (Serverless Compute)
* Amazon CloudWatch Logs (Monitoring & Logging)

#  Workflow

1. Upload a file to the S3 bucket
2. S3 generates an event (ObjectCreated)
3. Lambda function is triggered automatically
4. Lambda processes the event
5. Logs are stored in CloudWatch

#Lambda Function Code

python
def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']
    
    print("S3 Triggered 🚀")
    print("Uploaded file:", file_name)

    return {
        'file': file_name
    }


#Sample Output (CloudWatch Logs)

S3 Triggered 
Uploaded file: Ashok_Kumar_Kori_CV.pdf

# Key Features

* Fully serverless architecture
* Real-time event processing
* Automatic trigger using S3 events
* Logging and monitoring with CloudWatch
* Scalable and cost-efficient

# Use Cases

* Real-time file processing
* Image/video processing pipelines
* Log processing automation
* Data ingestion workflows

# Security & Permissions

* IAM Role with basic Lambda execution permissions
* S3 bucket configured with event notifications
* No public access enabled


# Cost Optimization

* Uses AWS Free Tier (Lambda + S3)
* Minimal execution time
* No always-running servers

# Future Improvements

* Integrate with API Gateway
* Add SNS/SQS notifications
* Store processed data in DynamoDB
* Add CI/CD pipeline

---

##  Author

Ashok Kumar Kori



This project demonstrates how to build a **scalable, event-driven system** using AWS serverless services.
