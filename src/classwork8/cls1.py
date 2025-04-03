# 1. Տրված է N x N չափերի երկչափ զանգված, որը ներկայացնում է ուղորդված գրաֆ։
# Վերադարձնել True, եթե գրաֆի յուրաքանչյուր գագաթի համար մտնող և դուրս եկող կողերի քանակները հավասար են,
# հակառակ դեպքում վերադարձնել False:

from typing import List


def is_i_o_edges_equal_nodes(matrix):
    edges_input_count_per_node = {}
    edges_output_count_per_node = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                edges_input_count_per_node[j] = edges_input_count_per_node.get(j, 0) + 1
                edges_output_count_per_node[i] = edges_output_count_per_node.get(i, 0) + 1

    print(edges_input_count_per_node, edges_output_count_per_node)
    for key in edges_input_count_per_node.keys():
        if edges_input_count_per_node.get(key) != edges_output_count_per_node.get(key):
            return False
    for key in edges_output_count_per_node.keys():
        if edges_output_count_per_node.get(key) != edges_input_count_per_node.get(key):
            return False

    return True


def graph_from_matrix_to_list(matrix: List[List[int]]):
    list_presentation = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                list_presentation.append(f'{i}->{j}')

    return list_presentation


if __name__ == "__main__":
    graph_matrix = [[0 for _ in range(10)] for _ in range(10)]
    graph_matrix[3][4] = 1
    graph_matrix[4][5] = 1
    graph_matrix[5][6] = 1
    graph_matrix[6][3] = 1
    for row in graph_matrix:
        print(row)
    print(is_i_o_edges_equal_nodes(graph_matrix))
