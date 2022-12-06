import os
import json
import requests


def lambda_handler(event, context):
    # forward request
    body = json.loads(event['body'])
    events = []
    for ev in body['request_data']['records']:
        event = {
            'device_id': body['network_headers']['device_id'],
            'network_id': body['network_headers']['network_id'],
            'account_id': body['network_headers']['account_id'],
            'timestamp': ev['timestamp'],
            'event_type': ev['event_type'],
            'event_value': ev['event_value'],
        }
        events.append(event)

    requests.post(os.environ.get('HANDLER'), json=events)
    print("Posted {} to {}".format(events, os.environ.get('HANDLER')))
    return dict(statusCode=200)
