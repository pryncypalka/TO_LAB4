from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, parent, name):
        self._parent = parent
        self._name = name

    @abstractmethod
    def get_parent(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

