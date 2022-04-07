from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from webargs.flaskparser import use_args

from crewbite.handlers import handlers
from crewbite.structures.errors import ClientError
from crewbite.structures.errors import ServerError
from werkzeug.exceptions import HTTPException

import logging
from logging.handlers import RotatingFileHandler

# EB looks for an 'application' callable by default.
application = Flask("CrewbiteAPI")
CORS(application)


@application.errorhandler(ClientError)
def handle_client_error(error):
    error_obj = error.to_dict()
    response = jsonify(error_obj)
    response.status_code = error.status_code
    logger.error(error_obj)
    return response


@application.errorhandler(ServerError)
def handle_server_error(error):
    error_obj = error.to_dict()
    response = jsonify(error_obj)
    response.status_code = error.status_code
    logger.error(error_obj)
    return response


@application.errorhandler(HTTPException)
def handle_error(error):
    # We do not log common client errors
    return {"msg": error.description}, error.code


@application.route("/")
def root():
    return "<h1>Welcome to the Crewbite API! You're not supposed to call the root API /</h1>"


@application.route("/status", methods=["GET"])
@use_args({})
def status(args):
    return handlers.Status(args)(request)


@application.route("/this-is-a-public-api", methods=["GET"])
@use_args({})
def public_api_test(args):
    return handlers.ThisIsAPublicAPI(args)(request)


@application.route("/this-is-an-authorized-api", methods=["GET"])
@use_args({})
def authorized_api_test(args):
    return handlers.ThisIsAnAuthorizedAPI(args)(request)


if __name__ == "__main__":
    # Local execution detected
    logging.basicConfig(level=logging.INFO)
    base_logger = logging.getLogger()
    handler = RotatingFileHandler("localLog.log", maxBytes=1024 * 1024 * 500, backupCount=3)
    base_logger.addHandler(handler)

    logger = logging.getLogger(__name__)
    logger.info("Crewbite local logger initiation complete.")
    application.run(host="127.0.0.1", port=5000)
else:
    # Elastic Beanstalk execution detected
    logging.basicConfig(level=logging.INFO)
    base_logger = logging.getLogger()
    handler = RotatingFileHandler("/opt/log/crewbite_api_service", maxBytes=1024*1024*500, backupCount=3)
    base_logger.addHandler(handler)
    logger = logging.getLogger(__name__)
    logger.info("Crewbite logger initiation complete.")
