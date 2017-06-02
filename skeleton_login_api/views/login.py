from flask import request, Blueprint, jsonify, current_app
from oauth2client import client, crypt
from skeleton_login_api.sql import Sql

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

        # check for required keys in google responce to complete login
        if "email_verified" in idinfo and idinfo["email_verified"] == True:
            user = {}
            user["email"] = idinfo["email"]
            user["google_id"] = idinfo["sub"]

            #check if user alredy exists
            #if not add them to the database
            users_check = Sql.get_user(user)
            if len(users_check) == 1:
                return jsonify(users_check[0].to_dict())
            elif len(users_check) == 0:
                new_user = Sql.new_user(user)

                #check that the new user has been created successfully
                if len(new_user) == 1:
                    return jsonify(new_user[0].to_dict())
                else:
                    raise ValueError('something has gone wrong creating a new user')
            else:
                #if more than 1 user has been found with the same details raise an error
                raise ValueError('something has gone wrong logging you in')
        else:
            raise ValueError('email has not been verified')
    else:
      raise ValueError('token missing')
