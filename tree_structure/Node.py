from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, parent, name):
        self._parent = parent
        self._name = name

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def create_memento(self):
        pass

    @abstractmethod
    def restore(self, memento):
        pass
