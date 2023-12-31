from Parser import Parser
from Config import Config
from Path_to_Directory import Path_to_Directory


class Prompt:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Prompt, cls).__new__(cls)
            cls._instance.current_user = Config.username
            cls._instance.current_host = Config.hostname
            cls._instance.current_location = None
            cls._instance.parser = Parser()
        return cls._instance

    @staticmethod
    def get_input():
        return input(f"{Prompt._instance.current_user}@{Prompt._instance.current_host}:{Path_to_Directory.directory_to_path(Prompt._instance.current_location)}# ")
    @staticmethod
    def display_message(message):
        print(f"Message: {message}")

    @staticmethod
    def display_result(result):
        if result is not None:
            print(result)

    @classmethod
    def update_location(cls, new_location):
        cls._instance.current_location = new_location

    @staticmethod
    def run():
        while True:
            try:
                command_input = Prompt.get_input()


                if command_input.lower() == "exit":
                    Prompt.display_message("Exiting the prompt.")
                    break

                Prompt._instance.parser.parse_command(command_input, Prompt._instance.current_location)


            except SyntaxError as e:
                Prompt.display_message(f"Syntax Error: {str(e)}")
            except Exception as e:
                Prompt.display_message(f"Error: {str(e)}")
