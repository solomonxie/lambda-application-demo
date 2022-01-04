import json
from urllib import request


def get_ip():
    info = None
    try:
        resp = request.urlopen("http://ip-api.com/json/")
        raw = resp.read()
        info = json.loads(raw)
    except Exception as e:
        print(e)
    return info
