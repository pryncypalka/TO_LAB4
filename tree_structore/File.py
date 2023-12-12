from Node import Node

class File(Node):
    def __init__(self, name, size, date):

        self.name = name
        self.size = size
        self.date = date


    def __str__(self):
        return "Name: " + self.name + "\nSize: " + self.size + "\nDate: " + self.date + "\n"