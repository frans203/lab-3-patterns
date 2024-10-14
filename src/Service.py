from src.ServiceIF import ServiceIf
from src.SingleElement import SingleElement


class Service(SingleElement, ServiceIf):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('draw service')