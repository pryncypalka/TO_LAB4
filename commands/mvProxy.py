from commands.CommandExecutor import CommandExecutor


class MvProxy(CommandExecutor):
    def __init__(self, mv_command):
        self._mv_command = mv_command

    def execute(self, args):
        return self._mv_command.execute(args)
