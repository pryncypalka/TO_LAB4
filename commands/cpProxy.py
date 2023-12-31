from commands.CommandExecutor import CommandExecutor
from tree_structure.File import File
from Path_to_Directory import Path_to_Directory
from commands.cp import Cp


class CpProxy(CommandExecutor):
    def __init__(self):
        self._cp_command = Cp()

    def execute(self, args, current_directory):
        source_path = args[0]
        destination_path = args[1]
        # Resolve the source and destination directories
        directory_path = Path_to_Directory.get_directory_path(source_path, current_directory)
        source_directory = Path_to_Directory.path_to_directory(directory_path, current_directory)
        destination_directory = Path_to_Directory.path_to_directory(destination_path, current_directory)

        if source_directory is None or destination_directory is None:
            result = "Invalid source or destination path."

        source_filename = Path_to_Directory.get_filename(source_path)

        source_file = source_directory.get_children_by_name(source_filename)

        result = self._cp_command.execute([destination_directory, source_filename, source_file, destination_path], current_directory)

        if result is not None:
            print(result)