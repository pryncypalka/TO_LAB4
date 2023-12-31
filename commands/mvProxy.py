from commands.CommandExecutor import CommandExecutor
from Path_to_Directory import Path_to_Directory
from commands.mv import Mv
class MvProxy(CommandExecutor):
    def __init__(self):
        self._mv_command = Mv()

    def execute(self, args, current_directory):
        source_path = args[0]
        destination_path = args[1]

        # Resolve the source and destination directories
        source_directory_path = Path_to_Directory.get_directory_path(source_path, current_directory)
        source_directory = Path_to_Directory.path_to_directory(source_directory_path, current_directory)
        destination_directory = Path_to_Directory.path_to_directory(destination_path, current_directory)

        if source_directory is None or destination_directory is None:
            result = "Invalid source or destination path."
        else:
            source_filename = Path_to_Directory.get_filename(source_path)
            source_node = source_directory.get_children_by_name(source_filename)

            result = self._mv_command.execute([source_node, destination_directory, source_directory_path, destination_path], current_directory)

            if result is not None:
                print(result)
