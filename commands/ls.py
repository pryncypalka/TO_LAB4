from commands.CommandExecutor import CommandExecutor
from tree_structure.File import File
class Ls(CommandExecutor):

    def __init__(self):
        pass

    def execute(self, args, current_directory):

        children = current_directory.get_children()
        for child in children:
            if isinstance(child, File):
                print('\033[91m' + child.get_name() + '\033[0m')
            else:
                print(child.get_name())





