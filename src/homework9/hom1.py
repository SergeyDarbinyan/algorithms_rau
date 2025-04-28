# Graph դասում ավելացնել ֆունկցիա, որը`
# 1. Մուտքում ստանում է երկու գագաթների արժեքները, և վերադարձնում է այդ արժեքներով գագաթները միացնող որևէ ճանապարհ,
# եթե այդպիսին գոյություն ունի, հակառակ դեպքում վերադարձնում է դատարկ զանգված։ Օրինակ՝
# ■ [[A, B], [A, C], [B, C], [C, D], [D, E], [E, A]] գրաֆի,
# source = A, dest = E գագաթների համար պատասխանը պետք է լինի [A, B, C, D, E] կամ [A, C, D, E]։
# ■ [[A, B], [A, C], [B, C], [C, D], [D, E], [E, A]] գրաֆի,
# source = E, dest = A գագաթների համար պատասխանը պետք է լինի [] ։
from src.classwork9.graph import Graph
from src.classwork9.node import Node

if __name__ == "__main__":
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
    print(graph.find_path_bfs(n1,n3))
    print(graph.find_path_bfs(n3,n1))