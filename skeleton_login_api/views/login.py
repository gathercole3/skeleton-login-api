from flask import request, Blueprint, jsonify, current_app
from oauth2client import client, crypt
from skeleton_login_api.sql import Sql
from skeleton_login_api.exceptions import ApplicationError

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
            raise ApplicationError('invalid missing', 'unspecified')

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
                    raise ApplicationError('something has gone wrong creating a new user', 'unspecified')
            else:
                #if more than 1 user has been found with the same details raise an error
                raise ApplicationError('something has gone wrong logging you in', 'unspecified')
        else:
            raise ApplicationError('email has not been verified', 'unspecified')
    else:
      raise ApplicationError('token missing', 'unspecified')

@login.route("/verify_login", methods=['POST'])
def verify_login():
    json_data = request.json

    if 'email' in json_data.keys() and 'password' in json_data.keys():
        user = {}
        user["email"] = json_data["email"]
        user["password"] = json_data["password"]

        #check if user exists
        users_check = Sql.get_user(user)
        if len(users_check) == 1:
            return jsonify(users_check[0].to_dict())
        else:
            raise ApplicationError('no user has been found with this email and password combination', 'u001', )
    else:
      raise ApplicationError('email or password missing', 'unspecified')
