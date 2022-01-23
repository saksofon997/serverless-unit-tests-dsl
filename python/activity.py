import os
import requests


def handler(event, context):
    res = requests.get(os.environ["API_URL"])

    return {
        "statusCode": 200,
        "body": res.text
    }
