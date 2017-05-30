from flask import request, Blueprint, jsonify, current_app
from oauth2client import client, crypt

login = Blueprint('login', __name__)

@login.route("/verify_google_token", methods=['POST'])
def verify_google_token():
    json_data = request.json

    if 'token' in json_data.keys():
        try:
            idinfo = client.verify_id_token(json_data["token"], current_app.config["GOOGLE_CLIENT_ID"])
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")
        except crypt.AppIdentityError:
            raise ValueError('invalid missing')
        return jsonify(idinfo)
    else:
      raise ValueError('token missing')
