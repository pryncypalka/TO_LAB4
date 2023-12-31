from commands.CommandExecutor import CommandExecutor
from tree_structure.File import File
from tree_structure.Directory import Directory

class Cp(CommandExecutor):
    def __init__(self):
        pass

    def execute(self, args, current_directory):
        destination_directory = args[0]
        source_filename = args[1]
        source_file = args[2]
        destination_path = args[3]

        if source_file is not None and isinstance(source_file, File):
            if destination_directory.get_children_by_name(source_filename) is not None:
                return f"File '{source_filename}' already exists in '{destination_path}'."
            else:
                destination_directory.add_child(File(source_filename, destination_directory, source_file.get_content()))
            return f"File '{source_filename}' copied to '{destination_path}'."
        elif source_file is not None and isinstance(source_file, Directory):
            if destination_directory.get_children_by_name(source_filename) is not None:
                return f"Directory '{source_filename}' already exists in '{destination_path}'."
            else:
                destination_directory.add_child(Directory(source_filename, destination_directory))
                for child in source_file.get_children():
                    destination_directory.get_children_by_name(source_filename).add_child(child)
            return f"Directory '{source_filename}' copied to '{destination_path}'."
        else:
            return f"File '{source_filename}' not found."