from flask import request, Blueprint, jsonify, current_app

general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return jsonify({
        "app": current_app.config["APP_NAME"],
        "status": "OK",
        "headers": request.headers.to_list(),
    })
