from collections import deque
from typing import List

from src.classwork9.edge import Edge
from src.classwork9.node import Node
from src.classwork9.node_color_enum import Color


class Graph:
    def __init__(self):
        self.all_nodes: dict[int, Node] = {}
        self.in_edges: dict[int, set[Edge]] = {}
        self.out_edges: dict[int, set[Edge]] = {}

    def get_node(self, value: int) -> Node:
        return self.all_nodes.get(value)

    def add_node(self, node: Node) -> bool:
        if node.value not in self.all_nodes:
            self.all_nodes[node.value] = node
            return True
        return False

    def add_edge(self, source_node: Node, dest_node: Node, label: int) -> bool:
        if source_node.value not in self.all_nodes or dest_node.value not in self.all_nodes:
            return False

        edge = Edge(source_node, dest_node, label)
        self.in_edges.setdefault(dest_node.value, set()).add(edge)
        self.out_edges.setdefault(source_node.value, set()).add(edge)
        return True

    def get_all_nodes(self) -> set:
        return set(self.all_nodes.values())

    def get_next_nodes(self, node: Node) -> List[Node]:
        edges = self.out_edges.get(node.value, set())
        return [edge.destination for edge in edges]

    def bfs(self, start_node: Node) -> List[Node]:
        visited = set()
        result = []
        queue = deque()

        queue.append(start_node)
        visited.add(start_node.value)

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)

            for neighbor in self.get_next_nodes(current_node):
                if neighbor.value not in visited:
                    visited.add(neighbor.value)
                    queue.append(neighbor)

        return result

    def bfs_print(self, start_node: Node):
        bfs_result = self.bfs(start_node)
        print("\n BFS traversal starting from node", start_node.value, ":")
        print(" → ".join(map(str, bfs_result)))

    @staticmethod
    def from_adjacency_matrix(matrix):
        graph = Graph()

        for i in range(len(matrix)):
            node = Node(i + 1)
            graph.add_node(node)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                weight = matrix[i][j]
                if weight != 0:
                    source_node = graph.get_node(i + 1)
                    dest_node = graph.get_node(j + 1)
                    graph.add_edge(source_node, dest_node, weight)

        return graph

    @staticmethod
    def from_adjacency_list(adj_list: dict[int, List[set]]):
        graph = Graph()

        for node_value in adj_list.keys():
            node = Node(node_value)
            graph.add_node(node)

        for source_value, edges in adj_list.items():
            source_node = graph.get_node(source_value)
            for dest_value, weight in edges:
                dest_node = graph.get_node(dest_value)
                graph.add_edge(source_node, dest_node, weight)

        return graph

    def dfs_visit(self, node: Node):
        print(node.value)
        node.color = Color.GREEN
        for next_node in self.get_next_nodes(node):
            if next_node.color == Color.WHITE:
                self.dfs_visit(next_node)

        node.color = Color.BLACK

    def dfs(self, start_node: Node):
        result = []
        graph_nodes = list(self.get_all_nodes())

        if start_node:
            if start_node.color == Color.WHITE:
                self.dfs_visit(start_node)

        for node in graph_nodes:
            if node.color == Color.WHITE:
                self.dfs_visit(node)

    def dfs_collect(self, node: Node, dfs_result: list):
        # Mark the node as visited and add to result list
        node.color = Color.GREEN
        print(f"Visiting node: {node.value}")
        dfs_result.append(node.value)

        # Visit all adjacent nodes
        for next_node in self.get_next_nodes(node):
            if next_node.color == Color.WHITE:
                self.dfs_collect(next_node, dfs_result)

        # Mark the node as fully visited
        node.color = Color.BLACK
        print(f"Node {node.value} is now fully visited (BLACK)")

    def dfs_print(self, start_node: Node):
        # List to collect nodes in DFS order
        dfs_result = []

        # Run the DFS traversal
        self.dfs_collect(start_node, dfs_result)

        # Print the result in a readable format
        print("\nDFS traversal starting from node", start_node.value, ":")
        print(" → ".join(map(str, dfs_result)))