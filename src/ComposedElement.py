from typing import List

from src.ElementGraphIterator import ElementGraphIterator
from src.GraphElementIF import GraphElementIF


class ComposedElement(GraphElementIF):
    def __init__(self,
                 children: List[GraphElementIF]):
        super().__init__()
        self.children = children
        self.iterator = ElementGraphIterator(children)

    def add(self, child: GraphElementIF):
        self.children.append(child)

    def remove(self, child: GraphElementIF):
        self.children.remove(child)

    def getChildren(self):
        return self.children

    def draw(self):
        self.iterator.iterate()
