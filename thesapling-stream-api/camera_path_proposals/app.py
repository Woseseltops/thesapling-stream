import json
import os
import boto3

def lambda_handler(event, context):

    # Get the table name from environment variables
    table_name = os.environ['CAMERA_PATH_PROPOSALS_TABLE']

    if event['httpMethod'] == 'PUT':

        if event['resource'] == '/camera-path-proposals':

            # Get the camera position from the request
            database_item = {'creator': 'Woseseltops', 'id': 'proposal-1'}

        elif event['resource'] == '/camera-path-proposals/{camera-path-proposal-id}/vote':

            database_item = {'creator': 'Woseseltops', 'id': 'proposal-1#vote-1', 'upvote': True, 'voter': 'Suze'}

        # Add to the database
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        table.put_item(Item=database_item)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,PUT,GET,POST",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({
            "message": "hello world",
            "event": event
        }),
    }
