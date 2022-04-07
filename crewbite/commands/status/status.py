from crewbite.commands.command import Command


class Status(Command):
    def __call__(self):
        return {
            "message": "I'm alive!",
        }
