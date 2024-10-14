from src.GraphElementIF import GraphElementIF


class SingleElement(GraphElementIF):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('drawing')