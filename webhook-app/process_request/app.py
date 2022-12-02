import boto3
import json
import os
import urllib.parse
from datetime import datetime

from boto3.dynamodb.conditions import Key


def get_requests(event):
    identifier = event['path']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    response = table.query(
        KeyConditionExpression=Key('InstanceID').eq(identifier)
    )

    if not response.get('Items'):
        return {"statusCode": 404}
    requests = [i for i in response.get('Items')]

    return dict(statusCode=200, body=json.dumps(requests))


def post_request(event):
    print(event)
    response = None
    identifier = event['path']
    if event.get('queryStringParameters'):
        response = event['queryStringParameters'].get('response_json')
        if response:
            response = urllib.parse.unquote(response)

    body = json.loads(event['body'])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    table.put_item(
        Item={
            'InstanceID': identifier,
            'RequestTimestamp': str(datetime.now().isoformat()),
            'request': json.dumps(body),
        }
    )
    json_resp = json.dumps(body)
    if response:
        json_resp = response

    return dict(statusCode=200, body=json_resp)


def lambda_handler(event, context):
    print(event['httpMethod'])
    if event['httpMethod'] == "GET":
        return get_requests(event)
    else:
        return post_request(event)
