import json

from flask import jsonify
from flask import make_response
import boto3

from crewbite.commands.status import status
from crewbite.commands.test import test
import logging

from crewbite.configurations import configurations
from crewbite.structures.errors import ClientError

logger = logging.getLogger(__name__)
client = boto3.client('cognito-idp', configurations["aws_region"])


class Stub(object):
    def __call__(self):
        raise NotImplementedError


class Handler(object):
    command_class = Stub

    unprotected_endpoints = {
        "/status",
        "/this-is-a-public-api"
    }

    def __init__(self, args=None):
        self.args = args

    def __call__(self, request):
        # Logging should exclude server healthcheck calls
        if request.path != "/status":
            logger.info("-------------API called-------------\n"
                        + request.method + "\t" + request.path
                        + "\n-----------Request headers----------\n"
                        + "Headers: " + str(request.headers)
                        + "\n---------Request parameters---------\n"
                        + str(self.args))

        if request.path not in self.unprotected_endpoints:
            if "Authorization" not in request.headers:
                raise ClientError("You must be signed in to access this endpoint")
            token = request.headers["Authorization"][7:]
            user = client.get_user(AccessToken=token)

            logger.info("-------------(TEMP) Decoded payload from auth header-------------\n"
                        + json.dumps(user))
            self.args["auth_name"] = user["Username"]

        # The following code is for ALB-integrated cognito token translation, which is not supported yet.
        # ----Xia,Shiyang 2022-03-31

        # if "x-amzn-oidc-data" in request.headers:
        #    # Step 1: Get the key id from JWT headers (the kid field)
        #    encoded_jwt = request.headers['x-amzn-oidc-data']
        #    jwt_headers = encoded_jwt.split('.')[0]
        #    decoded_jwt_headers = base64.b64decode(jwt_headers).decode("utf-8")
        #    decoded_json = json.loads(decoded_jwt_headers)
        #    kid = decoded_json['kid']

        #    # Step 2: Get the public key from regional endpoint
        #    url = 'https://public-keys.auth.elb.us-east-1.amazonaws.com/' + kid
        #    req = requests.get(url)
        #    pub_key = req.text
        #    logger.info("-------------(TEMP) Kid retrieved-------------\n"
        #                + pub_key)

        #    # Step 3: Get the payload
        #    payload = jwt.decode(encoded_jwt, pub_key, algorithms=['ES256'])
        #    logger.info("-------------(TEMP) Decoded payload from auth header-------------\n"
        #                + json.dumps(payload))
        #    self.args["auth_name"] = payload["username"]

        result = self.command_class(self.args)()

        if request.path != "/status":
            logger.info("----------Request response---------\n"
                        + str(result))

        response = make_response(jsonify(result))
        return response


class Status(Handler):
    command_class = status.Status


class ThisIsAPublicAPI(Handler):
    command_class = test.ThisIsAPublicAPI


class ThisIsAnAuthorizedAPI(Handler):
    command_class = test.ThisIsAnAuthorizedAPI
