# 2. Տրված է N բնական թիվը և M x 2 չափերի երկչափ զանգված,
# որոնք նեկայացնում է չուղորդված գրաֆի գագաթների քանակն ու կողերի բազմությունը։
# Վերադարձնել գրաֆի այն կողերի բազմությունը, որոնք անհրաժեշտ են գրաֆը լրիվ գրաֆ դարձնելու համար։
from typing import List


def get_missing_edges_for_full_graph(n_tops: int, existing_edges: List[List[int]]) -> List[List[int]]:
    all_edges: List[List[int]] = []
    for i in range(n_tops):
        for j in range(i + 1, n_tops):
            all_edges.append([i, j])
    edges_to_return: List[List[int]] = []
    for i in all_edges:
        if i not in existing_edges and i[::-1] not in existing_edges:
            edges_to_return.append(i)
    return edges_to_return


def my_test_get_missing_edges(n_tops: int, existing_edges: List[List[int]]):
    needed_edges: List[List[int]] = get_missing_edges_for_full_graph(n_tops, existing_edges)
    print(f"Remaining edges for {n_tops} tops {existing_edges} graph : {needed_edges}\n")


def my_test_some_cases():
    my_test_get_missing_edges(6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
    my_test_get_missing_edges(5, [[0, 1], [4, 2], [3, 2]])
    my_test_get_missing_edges(8, [[1, 3], [2, 1], [2, 3], [4, 5]])


if __name__ == "__main__":
    my_test_some_cases()
