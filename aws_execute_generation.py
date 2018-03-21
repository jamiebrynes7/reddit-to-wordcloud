import matplotlib
matplotlib.use('Agg')   # Stops cloud failures due to looking for the _tkinter module

import boto3
import json
import base64
from io import BytesIO

from common_lib import generate_wordcloud, WordcloudSettings


ERROR_STRING = "ERROR: {0}"

def handler(event, context):

    body = json.loads(event['body'])
    wordcloud_settings = WordcloudSettings(**body["wordcloud_settings"]).add_url(body["url"])

    try:
        image = generate_wordcloud(wordcloud_settings)
        buffer = BytesIO()
        image.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        dynamo_db = boto3.resource("dynamodb")
        table = dynamo_db.Table("reddit_to_wordcloud")
        table.update_item(
            Key={
                "tag": body["db_tag"]
            },
            UpdateExpression="SET image = :image, status = :status",
            ExpressionAttributeValues={
                "image": img_str,
                "status": "done"
            }
        )
        return {"image": img_str}
    except Exception as e:
        dynamo_db = boto3.resource("dynamodb")
        table = dynamo_db.Table("reddit_to_wordcloud")
        table.update_item(
            Key={
                "tag": body["db_tag"]
            },
            UpdateExpression="SET image = :image, status = :status",
            ExpressionAttributeValues={
                "image": ERROR_STRING.format("Failed to generate wordcloud with error " + str(e)),
                "status": "error"
            }
        )
        return {"error": ERROR_STRING.format("Failed to generate wordcloud with error " + str(e))}