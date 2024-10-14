from src.ConnectionIF import ConnectionIF
from src.SingleElement import SingleElement


class Connection(ConnectionIF, SingleElement):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('draw Connection')