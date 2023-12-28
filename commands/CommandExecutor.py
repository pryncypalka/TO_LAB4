from abc import ABC, abstractmethod


class CommandExecutor(ABC):
    @abstractmethod
    def execute(self, args, current_directory):
        pass
