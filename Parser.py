from commands.CommandExecutor import CommandExecutor
from commands.cdProxy import CdProxy
from commands.lsProxy import LsProxy
from commands.touchProxy import TouchProxy
from commands.moreProxy import MoreProxy
from commands.cpProxy import CpProxy
from commands.mvProxy import MvProxy
from tree_structure.Directory import Directory


class Parser:
    def __init__(self, root_directory):
        self._root_directory = root_directory
        self._current_location = root_directory
    def parse_command(self, command_text, current_directory):
        tokens = command_text.split()
        self._current_location = current_directory


        if not tokens:
            raise SyntaxError("Empty command")

        command = tokens[0].lower()

        if command == "ls":
            self.parse_ls(tokens[1:])
        elif command == "cd":
            self.parse_cd(tokens[1:])
        elif command == "touch":
            self.parse_touch(tokens[1:])
        elif command == "more":
            self.parse_more(tokens[1:])
        elif command == "cp":
            self.parse_cp(tokens[1:])
        elif command == "mv":
            self.parse_mv(tokens[1:])
        else:
            raise SyntaxError(f"Unknown command: {command}")

    def parse_ls(self, args):
        if args:
            raise SyntaxError("ls command does not take any arguments")
        proxy_ls = LsProxy()
        proxy_ls.execute(args, self._current_location)

    def parse_cd(self, args):
        proxy_cd = CdProxy()
        proxy_cd.execute(args, self._current_location)

    def parse_touch(self, args):
        if not args:
            raise SyntaxError("touch command requires a filename argument")
        proxy_touch = TouchProxy()
        proxy_touch.execute(args, self._current_location)

    def parse_more(self, args):
        if not args:
            raise SyntaxError("more command requires a filename argument")
        proxy_more = MoreProxy()
        proxy_more.execute(args, self._current_location)

    def parse_cp(self, args):
        if len(args) != 2:
            raise SyntaxError("cp command requires two arguments: source and destination")
        proxy_cp = CpProxy()
        proxy_cp.execute(args, self._current_location)

    def parse_mv(self, args):
        if len(args) != 2:
            raise SyntaxError("mv command requires two arguments: source and destination")
        proxy_mv = MvProxy()
        proxy_mv.execute(args, self._current_location)

    def Path_to_directory(self, path):
        if not path:
            return self._root_directory  # Jeśli ścieżka jest pusta, zwróć korzeń

        current_directory = self._root_directory
        components = path.split("/")

        for component in components:
            if component == "..":
                # Przejście do rodzica
                current_directory = current_directory.get_parent()
            elif component == ".":
                # Pomijanie aktualnego katalogu
                continue
            else:
                # Przejście do potomka
                child_directory = current_directory.get_child_by_name(component)
                if child_directory is not None and isinstance(child_directory, Directory):
                    current_directory = child_directory
                else:
                    # Jeśli katalog nie istnieje, zwróć None lub obsłuż błąd
                    return None

        return current_directory
