from crewbite.commands.command import Command
from crewbite.configurations import configurations
from crewbite.structures.errors import ClientError


class ThisIsAPublicAPI(Command):
    def __call__(self):
        return {
            "owner_email": configurations["owner_email"]
        }


class ThisIsAnAuthorizedAPI(Command):
    def check_request(self):
        if "auth_name" not in self.args:
            raise ClientError("Not logged in")

    def __call__(self):
        return {
            "message": "Hi " + self.args["auth_name"] + "! Welcome to this post-Authorization page!"
        }
