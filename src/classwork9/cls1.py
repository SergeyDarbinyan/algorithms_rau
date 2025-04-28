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
#
# 1. Graph կլասսում ավելացնել dfs կատարող ֆունկցիա, նշել գագաթ մուտք գործելիս եւ գագաթից դուրս
# գալիս շրջանցման հերթականությունը։ (Node::start, Node::finish, Node::color).
# ➢ void dfs()


from src.classwork9.graph import Graph
from src.classwork9.node import Node


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

    print("\n Next nodes from Node(2):")
    next_nodes = graph.get_next_nodes(node2)
    for node in next_nodes:
        print(node.value)

    graph.bfs_print(node2)

    graph.dfs_print(node2)

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
