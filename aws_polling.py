import boto3

import json

def handler(event, context):

    body = json.loads(event['body'])

    dynamo_db = boto3.resource("dynamodb")
    table = dynamo_db.Table("reddit_to_wordcloud")

    item = table.get_item(Key={"tag": body["db_tag"]})

    if item["status"] == "done":
        return {"image": item["image"]}
    else:
        return {"status": item["status"]}