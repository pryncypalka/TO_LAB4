from commands.CommandExecutor import CommandExecutor


class MoreProxy(CommandExecutor):
    def __init__(self, more_command):
        self._more_command = more_command

    def execute(self, args):
        return self._more_command.execute(args)
