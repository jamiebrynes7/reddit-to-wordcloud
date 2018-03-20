import json
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
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
        return {"image": img_str}
    except Exception as e:
        return {"error": ERROR_STRING.format("Failed to generate wordcloud with error " + str(e))}