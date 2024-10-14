from src.ComposedElement import ComposedElement
from src.NetNodeCollectionIF import NetNodeCollectionIF


class NetNodeCollection(ComposedElement, NetNodeCollectionIF):
    def __init__(self, children):
        super().__init__(children=children)

