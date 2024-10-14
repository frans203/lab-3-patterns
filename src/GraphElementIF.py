from abc import ABC, abstractmethod


class GraphElementIF(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass