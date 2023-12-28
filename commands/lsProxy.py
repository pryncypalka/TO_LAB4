from commands.CommandExecutor import CommandExecutor


class LsProxy(CommandExecutor):
    def __init__(self, ls_command):
        self._ls_command = ls_command

    def execute(self, args):
        return self._ls_command.execute(args)
