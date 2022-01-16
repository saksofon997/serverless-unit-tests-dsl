import json
import os


def handler(event, context):
    if "BadHeader" in event["headers"]:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Bad Request!",
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": os.environ["HELLO"],
        }),
    }
