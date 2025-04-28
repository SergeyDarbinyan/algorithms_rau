from src.classwork9.node import Node


class Edge:
    def __init__(self, source, destination, label):
        self.source: Node = source
        self.destination: Node = destination
        self.label: int = label

    def __hash__(self):
        return hash((self.source.value, self.destination.value, self.label))

    def __eq__(self, other):
        return (self.source.value, self.destination.value, self.label) == \
            (other.source.value, other.destination.value, other.label)

    def __repr__(self):
        return f"Edge({self.source.value} -> {self.destination.value}, label={self.label})"
