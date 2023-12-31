from commands.CommandExecutor import CommandExecutor
from tree_structure.File import File

from tree_structure.Directory import Directory
class Mv(CommandExecutor):
    def __init__(self):
        pass

    def execute(self, args, current_directory):
        source_node = args[0]
        destination_directory = args[1]
        source_directory_path = args[2]
        destination_path = args[3]


        if source_node is not None and isinstance(source_node, File):
            if destination_directory.get_children_by_name(source_node.get_name()) is not None:
                return f"Node '{source_node.get_name()}' already exists in '{destination_path}'."
            else:

                destination_directory.add_child(File(source_node.get_name(), destination_directory, source_node.get_content()))
                source_node.get_parent().remove_child(source_node)
                return f"Node '{source_node.get_name()}' moved to '{destination_path}'."
        elif source_node is not None and isinstance(source_node, Directory):
            if destination_directory.get_children_by_name(source_node.get_name()) is not None:
                return f"Node '{source_node.get_name()}' already exists in '{destination_path}'."
            else:
                destination_directory.add_child(Directory(source_node.get_name(), destination_directory))
                source_node.get_parent().remove_child(source_node)
                return f"Node '{source_node.get_name()}' moved to '{destination_path}'."
        else:

            return f"Node '{source_node.get_name()}' not found."