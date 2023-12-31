from tree_structure.Node import Node


class File(Node):
    def __init__(self, name, parent, content=""):
        super().__init__(parent, name)
        self._content = content

    def get_parent(self):
        return self._parent

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def get_name(self):
        return self._name


