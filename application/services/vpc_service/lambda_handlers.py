import json
from urllib import request


def get_myip():
    resp = request.urlopen('http://ip-api.com/json/')
    raw = resp.read()
    return raw


def vpn_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello VPC from:\n{}".format(get_myip()),
        }),
    }
