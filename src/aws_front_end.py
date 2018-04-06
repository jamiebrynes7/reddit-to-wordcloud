import boto3
from requests_futures.sessions import FuturesSession

import json
import random
import os
import string
import time

def random_id(length):
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for i in range(length))


def handler(event, context):

    body = json.loads(event['body'])

    # Generate a random key
    tag = random_id(25)
    body["db_tag"] = tag

    # Insert a new row into dynamo db
    dynamo_db = boto3.resource("dynamodb")
    table = dynamo_db.Table("reddit_to_wordcloud")
    table.put_item(
        Item={
            "tag": tag,
            "status": "working",
            "image": "placeholder"
        }
    )

    # Trigger execution lambda
    session = FuturesSession()
    session.post("https://qirlhy4te6.execute-api.eu-west-2.amazonaws.com/production/reddit-to-wordcloud-execute", json=body)
    
    time.sleep(3) # Wait for the request to successfully transmit

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "status": "working", 
            "db_tag": tag
        })
    }

    return response
