import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')

    queue = sqs.Queue(url='https://sqs.us-east-1.amazonaws.com/860368004749/cs5260-requests')
    response = queue.send_message(MessageBody=json.dumps(event))
        
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }