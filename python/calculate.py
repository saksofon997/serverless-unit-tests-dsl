import os


def handler(event, context):
    print(event)
    print(os.environ)
    if (os.environ["OPERATION"] == "add"):
        return event["a"] + event["b"]
    elif (os.environ["OPERATION"] == "multiply"):
        return event["a"] * event["b"]
