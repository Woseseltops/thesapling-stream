import json
import requests
import boto3

def lambda_handler(event, context):

    # Add a camera position to dynomoDB

    TABLE_NAME = 'CameraPositions'

    # Get the camera position from the request
    database_item = {'creator': 'Woseseltops', 'id': 'proposal-1'}

    # Add the camera position to the database
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=database_item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
