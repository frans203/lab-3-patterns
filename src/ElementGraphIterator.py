from src.ElementGraphIteratorIF import ElementGraphIteratorIF
from src.GraphElementIF import GraphElementIF
from typing import List


class ElementGraphIterator(ElementGraphIteratorIF):
    def __init__(self, children: List[GraphElementIF]):
        super().__init__()
        self.children = children

    def iterate(self):
        for child in self.children:
            child.draw()