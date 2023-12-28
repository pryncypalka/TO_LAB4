from commands.CommandExecutor import CommandExecutor
from commands.cd import Cd
from Parser import Parser


class CdProxy(CommandExecutor):
    def __init__(self):
        self._cd_command = Cd()

    def execute(self, args, current_directory):
        if not args:
            # Jeśli brak argumentów, przenieś do katalogu /usr/admin
            target_directory = "/usr/admin"
        else:
            target_directory = args[0]

        if target_directory == "..":
            # Sprawdź, czy można się przenieść do docelowego katalogu
            if self.can_change_directory(target_directory):
                result = self._cd_command.execute([target_directory])
            else:
                result = f"Cannot change to {target_directory}. Directory does not exist."
        else:
            result = f"Invalid argument for cd command: {target_directory}"

        return result

    def can_change_directory(self, target_directory):
        pass

