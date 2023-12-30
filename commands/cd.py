from commands.CommandExecutor import CommandExecutor

class Cd(CommandExecutor):

    def __init__(self):
        pass

    def execute(self, directory, current_directory):
        from prompt import Prompt
        prompt = Prompt()
        prompt.update_location(directory)





