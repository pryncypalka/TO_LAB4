from commands.CommandExecutor import CommandExecutor
from tree_structure.File import File


class Touch(CommandExecutor):
    def __init__(self):
        pass

    def execute(self, file_name, current_directory):

        for child in current_directory.get_children():
            if child.get_name() == file_name:
                return f"File '{file_name}' already exists."
        current_directory.add_child(File(file_name, current_directory))
        return f"File '{file_name}' created."