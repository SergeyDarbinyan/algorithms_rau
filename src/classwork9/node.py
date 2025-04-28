from src.classwork9.node_color_enum import Color


class Node:
    def __init__(self, value):
        self.value: int = value
        self.color = Color.WHITE

    def __repr__(self):
        return f"Node({self.value})"
