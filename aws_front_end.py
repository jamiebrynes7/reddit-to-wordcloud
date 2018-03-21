import boto3
import requests

import json
import random
import random
import string

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
    table.insert_item(
        Item={
            "db_tag": tag,
            "status": "working",
            "image": ""
        }
    )

    # Trigger execution lambda
    requests.post(execution_lambda_url, json=body)

    return {"status": "working", "db_tag": tag}
