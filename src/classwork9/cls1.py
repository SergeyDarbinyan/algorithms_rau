class Node:
    def __init__(self, value):
        self.value: int = value


class Edge:
    def __init__(self, source, destination, label):
        self.source: Node = source
        self.destination: Node = destination
        self.label: int = label


class Graph:
    def __init__(self, all_nodes, in_edges, out_edges):
        self.all_nodes: dict[int, Node] = all_nodes
        self.in_edges: dict[int, set[Edge]] = in_edges
        self.out_edges: dict[int, set[Edge]] = out_edges

    def get_node(self, node):
        return self.all_nodes.get(node)

    def add_node(self, value):
        if value not in self.all_nodes.keys():
            node = Node(value)
            self.all_nodes[value] = node
            return True
        return False

    def add_edge(self, source, dest, label):
        edge = Edge(source, dest, label)
        result = False
        if edge.destination.value not in self.in_edges.keys():
            self.in_edges[edge.destination.value] = {edge, label}
            result = True
        if edge.source.value not in self.out_edges.keys():
            self.out_edges[edge.source.value] = {edge, label}
            result = True

        return result

    def get_all_nodes(self):
        return self.all_nodes.values()

    def get_next_nodes(self, node_value):
        edges = self.out_edges.get(node_value)
        next_nodes = []
        for i in edges:
            next_nodes.append(i)
        return next_nodes


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    edge1 = Edge(node1, node2, 3)
    edge2 = Edge(node2, node3, 4)
    graph = Graph({node1.value: node1, node2.value: node2, node3.value: node3, node4.value: node4},
                  {node2.value: {edge1, edge1.label}, node3.value: {edge2, edge2.label}},
                  {node1.value: {edge1, edge1.label}, node2.value: {edge2, edge2.label}})

    graph.add_node(5)
    print(graph.out_edges)

    all_nodes = graph.get_all_nodes()
    for node in all_nodes:
        print(node.value)

    next_nodes = graph.get_next_nodes(2)
    for node in next_nodes:
        print(node.value)
