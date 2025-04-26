# Ստեղծել Graph դաս, որի համար տրված է main.cpp ֆայլը․
# 1.Կառուցել Node <T> կլասսը, որը կպարունակի T value դաշտ
# 2.Կառուցել Edge <T, L> կլասսը, հետևյալ դաշտերով․
# ➢ Node <T> * source;
# ➢ Node <T> * destnaton;
# ➢ L label;
# 3.Կառուցել ուղղորդված Graph <T, L> կլասսը, հետևյալ դաշտերով.
# ➢ std :: unordered_map <T,Node <T>> allNodes
# ➢ std :: unordered_map <T,std :: unordered_set <Edge <T,L>>> inEdges
# ➢ std :: unordered_map <T,std :: unordered_set <Edge <T,L>>> outEdges
# 4.Graph կլասսում ավելացնել հետևյալ ֆունկցիները․
# ➢ Node <T> * getNode (constT&data)
# ➢ bool addNode(constT&v)
# ➢ bool addEdge(constT&source,constT&dest,constL&label)
# ➢ std :: unordered_set <T> getAllNodes() const
# ➢ std :: vector <T> getNextNodes(constT&nodeValue) const
# ➢ std :: vector <T> bfs(constT&start)
# ➢ void bfsPrint(constT&start)
# 5.Ավելացնել ֆունկցիա, որ գրաֆի մատրիցային ներկայացումից կստեղծի մեր Graph<int, int> տիպի օբյեկտ։
# 6.Ավելացնել ֆունկցիա, որ գրաֆի հարևանության ցուցակ ներկայացումից
# (adjacency-list representaton) կստեղծի մեր Graph<int, int> տիպի օբյեկտ։
# 1. Graph կլասսում ավելացնել dfs կատարող ֆունկցիա, նշել գագաթ մուտք գործելիս եւ գագաթից դուրս
# գալիս շրջանցման հերթականությունը։ (Node::start, Node::finish, Node::color).
# ➢ void dfs()

from collections import deque
from typing import List

from src.classwork9.node_color_enum import Color


class Node:
    def __init__(self, value):
        self.value: int = value
        self.color = Color.WHITE

    def __repr__(self):
        return f"Node({self.value})"


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


def my_test_1():
    print("\n ----- Start my test 1 -----")
    graph = Graph()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    for node in [node1, node2, node3, node4]:
        graph.add_node(node)

    n1 = graph.get_node(1)
    n2 = graph.get_node(2)
    n3 = graph.get_node(3)
    n4 = graph.get_node(4)

    graph.add_edge(n1, n2, 3)
    graph.add_edge(n2, n3, 4)
    graph.add_edge(n3, n2, 2)
    graph.add_edge(n2, n1, 2)

    graph.add_node(Node(5))

    print("\n All nodes:")
    all_nodes = graph.get_all_nodes()
    for node in all_nodes:
        print(node.value)

    print("\n Ingoing edges:")
    for k, v in graph.in_edges.items():
        print(f"{k}: {v}")

    print("\n Outgoing edges:")
    for k, v in graph.out_edges.items():
        print(f"{k}: {v}")

    print("\n Next nodes Node(2)-ից:")
    next_nodes = graph.get_next_nodes(node2)
    for node in next_nodes:
        print(node.value)
    graph.bfs_print(node2)
    graph.dfs(node2)

    print("\n ----- End my test 1 -----")


def my_test_2():
    print("\n ----- Start my test 2 -----")

    matrix = [
        [0, 3, 0, 0, 0],
        [0, 0, 4, 0, 0],
        [0, 2, 0, 0, 0],
        [0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0]
    ]

    graph = Graph.from_adjacency_matrix(matrix)

    print("\n All nodes:")
    for node in graph.get_all_nodes():
        print(node)

    print("\n Ingoing edges:")
    for k, v in graph.in_edges.items():
        print(f"{k}: {v}")

    print("\n Outgoing edges:")
    for k, v in graph.out_edges.items():
        print(f"{k}: {v}")

    print("\n ----- End my test 2 -----")


def my_test_3():
    print("\n ----- Start my test 3 -----")

    adj_list = {
        1: [(2, 3)],
        2: [(3, 4)],
        3: [(2, 2)],
        4: [(5, 5)],
        5: []
    }

    graph = Graph.from_adjacency_list(adj_list)

    print("\n All nodes:")
    for node in graph.get_all_nodes():
        print(node.value)

    print("\n Ingoing edges:")
    for k, v in graph.in_edges.items():
        print(f"{k}: {v}")

    print("\n Outgoing edges:")
    for k, v in graph.out_edges.items():
        print(f"{k}: {v}")

    print("\n ----- End my test 3 -----")


if __name__ == "__main__":
    my_test_1()
    # my_test_2()
    # my_test_3()
