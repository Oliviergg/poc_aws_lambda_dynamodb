import os
import json
import boto3
from aws_lambda_powertools import Logger

logger = Logger(service="CreateProject")
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        item = {
            'id': data['id'],
            'value': data['value']
        }
        table.put_item(Item=item)
        response = {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except Exception as e:
        logger.exception(e)
        response = {
            'statusCode': 500,
            'body': 'An error occurred while processing your request.'
        }

    return response