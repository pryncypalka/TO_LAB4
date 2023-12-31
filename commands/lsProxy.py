from commands.CommandExecutor import CommandExecutor
from commands.ls import Ls
from Path_to_Directory import Path_to_Directory
class LsProxy(CommandExecutor):
    def __init__(self):
        self._ls_command = Ls()

    def execute(self, args, current_directory):
        if not args:
            return self._ls_command.execute(args, current_directory)
        else:
            target_directory = args[0]


        directory = Path_to_Directory.path_to_directory(target_directory, current_directory)
        if directory is not None:
            result = self._ls_command.execute(directory, directory)
        else:
            result = f"Directory does not exist."

            if result is not None:
                print(result)


