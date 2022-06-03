import requests
import json


def get_request(url, headers = {}, payload = {}):
    try:
        r = requests.get(url, headers = headers, data = json.dumps(payload))
    except:
        return 'Error'

    return r.json()


def post_request(url, headers = {}, payload = {}):
    try:
        r = requests.post(url, headers = headers, data = json.dumps(payload))
    except:
        return 'Error'

    return r.json()


def put_request(url, headers={}, payload={}):
    try:
        r = requests.put(url, headers=headers, data=json.dumps(payload))
    except:
        return 'Error'

    return r.json()
