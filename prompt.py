from Parser import Parser
from Config import Config


class Prompt:
    def __init__(self, root_directory):
        self.current_user = Config.username
        self.current_host = Config.hostname
        self.current_location = root_directory
        self.parser = Parser(root_directory)

    def get_input(self):
        return input(f"{self.current_user}@{self.current_host}:{self.current_location.get_name()}# ")


    def display_message(self, message):
        print(f"Message: {message}")

    def display_result(self, result):
        print(f"Result: {result}")

    def update_location(self, new_location):
        self.current_location = new_location

    def run(self):
        while True:
            try:
                command_input = self.get_input()

                if command_input.lower() == "exit":
                    self.display_message("Exiting the prompt.")
                    break

                result = self.parser.parse_command(command_input, self.current_location)
                self.display_result(result)

            except SyntaxError as e:
                self.display_message(f"Syntax Error: {str(e)}")
            except Exception as e:
                self.display_message(f"Error: {str(e)}")



