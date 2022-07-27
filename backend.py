import requests
import json


def get_request(url, headers=None, payload=None):
    try:
        r = requests.get(url, headers=headers, data=json.dumps(payload))

        try:
            return r.json()
        except requests.JSONDecodeError:
            return r.text

    except:
        return 'Error when attempting to make request'


def post_request(url, headers=None, payload=None):
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))

        try:
            return r.json()
        except requests.JSONDecodeError:
            return r.text

    except:
        return 'Error when attempting to make request'


def put_request(url, headers=None, payload=None):
    try:
        r = requests.put(url, headers=headers, data=json.dumps(payload))

        try:
            return r.json()
        except requests.JSONDecodeError:
            return r.text

    except:
        return 'Error when attempting to make request'
