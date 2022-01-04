import json
import requests


def status_handler(event, context):
    info = requests.get('http://ip-api.com/json/').json()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world, Status: OK",
            "location": info,
        }),
    }
