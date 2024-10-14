from src.ComposedElement import ComposedElement
from src.NetNodeIF import NetNodeIF


class NetNode(ComposedElement, NetNodeIF):
    def __init__(self, children):
        super().__init__(children=children)
