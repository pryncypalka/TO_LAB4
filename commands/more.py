
from commands.CommandExecutor import CommandExecutor
from tree_structure.File import File
class More(CommandExecutor):
    def __init__(self):
        pass

    def execute(self, filename, current_directory):

        file_to_display = current_directory.get_children_by_name(filename)

        if file_to_display is not None and isinstance(file_to_display, File):
            return file_to_display.get_content()
        else:
            return f"File '{filename}' not found."