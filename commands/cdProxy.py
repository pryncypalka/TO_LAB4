from commands.CommandExecutor import CommandExecutor
from commands.cd import Cd
from Path_to_Directory import Path_to_Directory


class CdProxy(CommandExecutor):
    def __init__(self):
        self._cd_command = Cd()

    def execute(self, args, current_directory):
        if not args:
            # Jeśli brak argumentów, przenieś do katalogu /usr/admin
            target_directory = "/usr/admin"
        else:
            target_directory = args[0]

        directory = Path_to_Directory.path_to_directory(target_directory, current_directory)
        if directory is not None:
            result = self._cd_command.execute(directory, current_directory)
        else:
            result = f"Cannot change to {target_directory}. Directory does not exist."

        if result is not None:
            print(result)





