
from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass

    @abstractmethod
    def show(self):
        pass


class Node(Base):

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = set()

    def add(self, obj):
        self.children.add(obj)
        obj.parent = self

    def remove(self, obj):
        self.children.remove(obj)
        obj.parent = None

    def show(self):
        print(self.name)
        for obj in self.children:
            obj.show()


if __name__ == "__main__":
    root = Node('root')
    node1 = Node('node1')
    node2 = Node('node2')
    node11 = Node('node11')
    node12 = Node('node12')

    root.add(node1)
    root.add(node2)
    node1.add(node11)
    node1.add(node12)

    root.show()

