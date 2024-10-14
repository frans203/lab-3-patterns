from src.ComposedElement import ComposedElement
from src.ServerIF import ServerIF


class Server(ComposedElement, ServerIF):
    def __init__(self, children):
        super().__init__(children=children)

