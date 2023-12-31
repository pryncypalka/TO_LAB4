from commands.CommandExecutor import CommandExecutor
from commands.more import More
from Path_to_Directory import Path_to_Directory


class MoreProxy(CommandExecutor):
    def __init__(self):
        self._more_command = More()

    def execute(self, args, current_directory):
        if not args:
            return "Usage: more <filename>"

        target_path = args[0]

        # Separate filename and directory path using the Path_to_Directory methods
        filename = Path_to_Directory.get_filename(target_path)
        directory_path = Path_to_Directory.get_directory_path(target_path, current_directory)
        # Resolve the target directory using the provided Path_to_Directory.path_to_directory method
        directory = Path_to_Directory.path_to_directory(directory_path, current_directory)
        if directory is not None:
            result = self._more_command.execute(filename, directory)
        else:
            result = "Directory does not exist."

        if result is not None:
            print(result)