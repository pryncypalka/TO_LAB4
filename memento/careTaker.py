from memento.Memento import Memento
from memento.MementoCollection import MementoCollection


class Caretaker:
    def __init__(self):
        self.__memento_collection = MementoCollection()

    def save_state(self, node):
        # Tworzymy memento na podstawie aktualnego stanu obiektu
        memento = Memento(node.get_name(), node.get_parent())
        self.__memento_collection.add_memento(memento)

    def restore_state(self, node):
        # Przywracamy stan obiektu na podstawie ostatniego memento
        last_memento = self.__memento_collection.get_last_memento()
        node.set_name(last_memento._name)
        node.set_parent(last_memento._parent)