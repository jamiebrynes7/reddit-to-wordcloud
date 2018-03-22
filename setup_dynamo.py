import boto3

dynamo_db = boto3.resource("dynamodb")

table = dynamo_db.create_table(
    TableName="reddit_to_wordcloud",
    KeySchema=[
        {
            "AttributeName": "tag",
            "KeyType": "HASH"
        }
    ],
    AttributeDefinitions=[
        {
            "AttributeName": "tag",
            "AttributeType": "S"
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName="reddit_to_wordcloud")

print("Table reddit_to_wordcloud created successfully")