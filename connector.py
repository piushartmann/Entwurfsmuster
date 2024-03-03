from flask import Flask, request, jsonify
import requests
import hashlib
import hmac
import base64
import json
import datetime
import pytz

app = Flask(__name__)

API_KEY = 'API_KEY'
HMAC_SECRET = "HMAC_SECRET"


def validate_api_key(key):
    return key == API_KEY


def generate_hmac_signature(data):
    message = bytes(data, 'utf-8')
    secret = bytes(HMAC_SECRET, 'utf-8')
    signature = hmac.new(secret, message, hashlib.sha1).digest()
    return base64.b64encode(signature).decode()


def send_request(path, data):
    BODY = data
    print(f"Path: {path} Data: {BODY}")
    signature = generate_hmac_signature(json.dumps(BODY))
    Headers = {
        "Accept": "application/json",
        "geofox-auth-type": "HmacSHA1",
        "geofox-auth-user": "geofox-api-user",
        "geofox-auth-signature": signature
    }
    print(BODY)
    response = requests.post(f"https://gti.geofox.de/{path}",
                             headers=Headers,
                             json=BODY)
    print(response.request.body, response.request.headers)
    print(response.json, response.headers)

    return jsonify(response.json()), response.status_code


@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def anyPath(path):
    api_key = request.headers.get('X-Api-Key')
    if not validate_api_key(api_key):
        return jsonify({'error': 'Invalid API key'}), 401
    try:
        json_string = request.get_json(force=True)
    except Exception:
        json_string = json.loads("{}")
    print(json_string)

    return send_request(path, json_string)


@app.route('/getTime', methods=['POST'])
def GetTime():
    api_key = request.headers.get('X-Api-Key')
    if not validate_api_key(api_key):
        return jsonify({'error': 'Invalid API key'}), 401

    current_date = datetime.datetime.now(pytz.timezone('Middle European Time'))
    date = current_date.strftime("%d.%m.%Y")
    time = current_date.strftime("%H:%M")
    current_time = {"date": date, "time": time}

    return jsonify(current_time), 200


if __name__ == '__main__':
    app.run(debug=True)
