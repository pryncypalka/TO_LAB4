from tree_structure.Directory import Directory
class Path_to_Directory:
    _root_directory = None

    @classmethod
    def path_to_directory(cls, path, current_directory=None):
        if not path:
            return cls._root_directory

        if current_directory is None:
            current_directory = cls._root_directory

        if path == "/":
            return cls._root_directory

        components = path.split("/")
        if path[0] == "/":
            current_directory = cls._root_directory
            components = components[1:]

        for component in components:
            if component == "..":
                # Przejście do rodzica
                current_directory = current_directory.get_parent()
                if current_directory is None:
                    raise ValueError(f"Invalid path: {path}")
            elif component == ".":
                continue
            else:
                # Przejście do potomka
                child_directory = current_directory.get_children_by_name(component)

                if child_directory is not None and isinstance(child_directory, Directory):
                    current_directory = child_directory
                else:
                    raise ValueError(f"Directory not found: {component}")

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

    @staticmethod
    def get_filename(path):
        # Split the path and return the last component as the filename
        components = path.split("/")
        return components[-1]

    @staticmethod
    def get_directory_path(path, current_directory):
        # Join all components except the last one to get the directory path

        components = path.split("/")
        directory_path = "/".join(components[:-1])


        if directory_path == "" and path[0] == "/":
            directory_path = "/"
        else:
            directory_path = Path_to_Directory.directory_to_path(current_directory)
        return directory_path
