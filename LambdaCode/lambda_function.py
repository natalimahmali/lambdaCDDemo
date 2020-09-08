import boto3
import json

def lambda_handler(event, context):
    response = "Hello from BioBeat's first CICD Lambda function!"
    return {"statusCode": 200, "body": json.dumps(response)}