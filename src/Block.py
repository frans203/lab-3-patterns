from abc import ABC

from src.BlockIF import BlockIF
from src.SingleElement import SingleElement


class Block(SingleElement, BlockIF, ABC):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('draw Block')