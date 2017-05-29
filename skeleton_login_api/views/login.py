from flask import request, Blueprint, jsonify, current_app

login = Blueprint('login', __name__)

@login.route("/verify_google_token", methods=['POST'])
def verify_google_token():
    return jsonify({
        "app": current_app.config["APP_NAME"],
        "status": "OK",
        "headers": request.headers.to_list(),
    })
