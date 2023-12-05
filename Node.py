from ABC import ABC, abstractmethod
class Node:
    def __init__(self,parent,name):
        self._parent = parent
        self._name = name



    def clone(self):
        pass

    def create_memento(self):
        pass
    def restore(self, memento):
        pass
