from tree_structure.Directory import Directory
class Path_to_Directory:
    _root_directory = None

    @classmethod
    def path_to_directory(cls, path):
        if not path:
            return cls._root_directory

        current_directory = cls._root_directory
        components = path.split("/")

        if path[0] == "/":
            current_directory = cls._root_directory
            components = components[1:]

        for component in components:
            if component == "..":
                # Przejście do rodzica
                current_directory = current_directory.get_parent()
            elif component == ".":

                continue
            else:
                # Przejście do potomka
                child_directory = current_directory.get_children_by_name(component)

                if child_directory is not None and isinstance(child_directory, Directory):
                    current_directory = child_directory
                else:
                    return None

        return current_directory

    @classmethod
    def directory_to_path(cls, directory):
        path = ""

        if isinstance(directory, Directory):
            if directory.get_name() == "/":
                return "/"
            while directory.get_parent() is not None:
                path = "/" + directory.get_name() + path
                directory = directory.get_parent()
            return path
        else:
            return None
