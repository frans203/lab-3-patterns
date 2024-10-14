from src.Block import Block
from src.ComposedElement import ComposedElement
from src.Connection import Connection
from src.NetNode import NetNode
from src.NetNodeCollection import NetNodeCollection
from src.Server import Server
from src.Service import Service

if __name__ == '__main__':
    composed_element = ComposedElement(children=[Connection(),
                                                 Server(children=[Connection()]),
                                                 NetNode(children=[Connection()]),
                                                 Service(),
                                                 NetNodeCollection(children=[Connection()]),
                                                 NetNodeCollection(children=[Service(), Block()])])
    composed_element.draw()