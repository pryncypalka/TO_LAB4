from Path_to_Directory import Path_to_Directory
from commands.CommandExecutor import CommandExecutor
from commands.touch import Touch

class TouchProxy(CommandExecutor):
    def __init__(self):
        self._touch_command = Touch()

    def execute(self, args, current_directory):

        target_path = args[0]

        # Separate filename and directory path
        filename = Path_to_Directory.get_filename(target_path)
        directory_path = Path_to_Directory.get_directory_path(target_path)

        # Resolve the target directory using the provided Path_to_Directory.path_to_directory method
        directory = Path_to_Directory.path_to_directory(directory_path, current_directory)

        if directory is not None:
            result = self._touch_command.execute(filename, directory)
        else:
            result = "Directory does not exist."

        if result is not None:
            print(result)