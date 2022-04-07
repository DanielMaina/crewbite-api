class Command(object):
    def check_request(self):
        pass

    def __init__(self, args=None):
        self.args = args
        self.check_request()
