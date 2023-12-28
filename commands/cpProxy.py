from commands.CommandExecutor import CommandExecutor


class CpProxy(CommandExecutor):
    def __init__(self, cp_command):
        self._cp_command = cp_command

    def execute(self, args, current_directory):

        return self._cp_command.execute(args,current_directory)