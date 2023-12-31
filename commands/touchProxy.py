from Path_to_Directory import Path_to_Directory
from commands.CommandExecutor import CommandExecutor
from commands.touch import Touch
import re


class TouchProxy(CommandExecutor):
    def __init__(self):
        self._touch_command = Touch()

    def execute(self, args, current_directory):

        target_path = args[0]

        # Separate filename and directory path
        filename = Path_to_Directory.get_filename(target_path)
        directory_path = Path_to_Directory.get_directory_path(target_path, current_directory)

        # Resolve the target directory using the provided Path_to_Directory.path_to_directory method
        directory = Path_to_Directory.path_to_directory(directory_path, current_directory)

        if directory is None:
            result = "Directory does not exist."
        elif not self.is_valid_linux_filename(filename):
            result = "Invalid File name."
        else:
            result = self._touch_command.execute(filename, directory)

        if result is not None:
            print(result)

    def is_valid_linux_filename(self, filename):
        # Wymagane: Dokładnie jedna litera lub cyfra jako pierwszy znak
        # Dozwolone znaki: Alfanumeryczne, kropki, myślniki, podkreślenia
        # Kropki są dozwolone, ale nie mogą występować po sobie
        pattern = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._-]*$')

        return bool(re.match(pattern, filename))
