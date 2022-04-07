class ClientError(Exception):
    status_code = 400

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message or "You've sent a bad request"
        self.status_code = status_code or ClientError.status_code
        self.payload = payload or {}

    def to_dict(self):
        error = dict(self.payload)
        error["message"] = self.message
        return error


class ServerError(Exception):
    status_code = 500

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message or "The server is confused. Please ping Xia Shiyang with steps to reproduce the error."
        self.status_code = status_code or ServerError.status_code
        self.payload = payload or {}

    def to_dict(self):
        error = dict(self.payload)
        error["message"] = self.message
        return error

