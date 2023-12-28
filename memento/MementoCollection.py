

class MementoCollection:
    def __init__(self):
        self.__mementos = []

    def add_memento(self, memento):
        self.__mementos.append(memento)

    def get_memento(self, index):
        return self.__mementos[index]

    def get_mementos(self):
        return self.__mementos

    def get_last_memento(self):
        return self.__mementos[-1]
