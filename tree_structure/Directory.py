from tree_structure.Node import Node


class Directory(Node):

    def __init__(self, name, parent):
        super().__init__(parent, name)
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def remove_child(self, child):
        self._children.remove(child)

    def get_children_by_name(self, name):
        return [child for child in self._children if child.get_name() == name]


    def get_name(self):
        return self._name

    def get_parent(self):
        return self._parent

    def clone(self):
        return Directory(self._name, self._parent)

    def create_memento(self):
        pass

    def restore(self, memento):
        pass
