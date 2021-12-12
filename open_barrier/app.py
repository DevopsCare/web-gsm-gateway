import json
import os

import boto3
from mypy_boto3_dynamodb import DynamoDBClient
from utils import open_barrier, notify_via_telegram

client: DynamoDBClient = boto3.client("dynamodb")


def lambda_handler(event, context):
    try:
        visitor = event['pathParameters']['name']
    except KeyError:
        return {
            "statusCode": 403,
            "body": json.dumps({
                "message": "Please authenticate first",
            })}

    visitor_data = client.get_item(TableName=os.environ['TABLE_NAME'], Key={'id': {'S': visitor}})
    # print(visitor_data)

    if 'Item' not in visitor_data:
        return {
            "statusCode": 403,
            "body": json.dumps({
                "message": "I don't know you",
            })}

    if 'chat_id' in visitor_data['Item']:
        notify_via_telegram(visitor_data['Item']['chat_id']['N'], visitor)

    if 'caller_id' not in visitor_data['Item']:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "visitor": visitor,
                "error": "invalid caller configuration"
            }),
        }

    opening = open_barrier(visitor_data['Item']['caller_id']['S'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "visitor": visitor,
            "barrier": "OPENING" if opening else "FAILED"
        }),
    }
