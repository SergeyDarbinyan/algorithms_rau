import unittest

from datetime import datetime
from typing import List


# Simple solution without optimization
def knap_sack_recursive(n: int, w: int, profit_list: List[int], weight_list: List[int]) -> int:
    if w == 0 or n == 0:
        return 0

    if weight_list[n - 1] > w:
        return knap_sack_recursive(n - 1, w, profit_list, weight_list)
    else:
        return max(profit_list[n - 1] + knap_sack_recursive(n - 1, w - weight_list[n - 1], profit_list, weight_list),
                   knap_sack_recursive(n - 1, w, profit_list, weight_list))


def knap_sack_with_memoization(n, w, profit_list: List[int], weight_list: List[int], memo: List[List[int]]) -> int:
    if w == 0 or n == 0:
        return 0

    if memo[n][w] != -1:
        return memo[n][w]

    if weight_list[n - 1] > w:
        memo[n][w] = knap_sack_with_memoization(n - 1, w, profit_list, weight_list, memo)
    else:
        memo[n][w] = max(
            profit_list[n - 1] + knap_sack_with_memoization(n - 1, w - weight_list[n - 1], profit_list, weight_list,
                                                            memo),
            knap_sack_with_memoization(n - 1, w, profit_list, weight_list, memo))
    return memo[n][w]


class TestKnapsack(unittest.TestCase):

    def setUp(self):
        self.profit_list_1 = [60, 100, 120, 40, 20, 30]
        self.weight_list_1 = [10, 20, 30, 15, 5, 12]
        self.capacity_1 = 50
        self.expected_result_1 = 220

        self.profit_list_2 = [10, 20, 30]
        self.weight_list_2 = [1, 2, 3]
        self.capacity_2 = 4
        self.expected_result_2 = 40

        self.profit_list_3 = [60, 100, 120]
        self.weight_list_3 = [10, 20, 30]
        self.capacity_3 = 50
        self.expected_result_3 = 220

        self.profit_list_4 = [i * 10 for i in range(1, 25)]
        self.weight_list_4 = [i for i in range(1, 25)]
        self.capacity_4 = 500
        self.expected_result_4 = 3000

    def test_knap_sack_recursive(self):
        result_1 = knap_sack_recursive(len(self.profit_list_1), self.capacity_1, self.profit_list_1,
                                       self.weight_list_1)
        self.assertEqual(result_1, self.expected_result_1)

        result_2 = knap_sack_recursive(len(self.profit_list_2), self.capacity_2, self.profit_list_2,
                                       self.weight_list_2)
        self.assertEqual(result_2, self.expected_result_2)

        result_3 = knap_sack_recursive(len(self.profit_list_3), self.capacity_3, self.profit_list_3,
                                       self.weight_list_3)
        self.assertEqual(result_3, self.expected_result_3)

    def test_knap_sack_with_memoization(self):
        memo_1 = [[-1 for _ in range(self.capacity_1 + 1)] for _ in range(len(self.profit_list_1) + 1)]
        result_1 = knap_sack_with_memoization(len(self.profit_list_1), self.capacity_1, self.profit_list_1,
                                              self.weight_list_1, memo_1)
        self.assertEqual(result_1, self.expected_result_1)

        memo_2 = [[-1 for _ in range(self.capacity_2 + 1)] for _ in range(len(self.profit_list_2) + 1)]
        result_2 = knap_sack_with_memoization(len(self.profit_list_2), self.capacity_2, self.profit_list_2,
                                              self.weight_list_2, memo_2)
        self.assertEqual(result_2, self.expected_result_2)

        memo_3 = [[-1 for _ in range(self.capacity_3 + 1)] for _ in range(len(self.profit_list_3) + 1)]
        result_3 = knap_sack_with_memoization(len(self.profit_list_3), self.capacity_3, self.profit_list_3,
                                              self.weight_list_3, memo_3)
        self.assertEqual(result_3, self.expected_result_3)

    def test_knap_sack_time(self):
        start_time = datetime.now()
        knap_sack_recursive(len(self.profit_list_4), self.capacity_4, self.profit_list_4, self.weight_list_4)
        duration_recursive = datetime.now() - start_time

        start_time = datetime.now()
        memo_4 = [[-1 for _ in range(self.capacity_4 + 1)] for _ in range(len(self.profit_list_4) + 1)]
        knap_sack_with_memoization(len(self.profit_list_4), self.capacity_4, self.profit_list_4, self.weight_list_4,
                                   memo_4)
        duration_memoization = datetime.now() - start_time

        print(f"Recursive Duration: {duration_recursive}")
        print(f"Memoization Duration: {duration_memoization}")


if __name__ == "__main__":
    unittest.main()

#
# def test_knap_sack_recursive(w: int, profit_list: List[int], weight_list: List[int]):
#     start_time: datetime = datetime.now()
#     knap_sack: int = knap_sack_recursive(len(profit_list), w, profit_list, weight_list)
#     print(f"Duration: {datetime.now() - start_time} (without optimization). KnapSack for {w} : {knap_sack}")
#
#
# def test_knap_sack_with_memoization(w: int, profit_list: List[int], weight_list: List[int]):
#     start_time: datetime = datetime.now()
#     memo: List[List[int]] = [[-1 for _ in range(w + 1)] for _ in range(len(profit_list) + 1)]
#     knap_sack: int = knap_sack_with_memoization(len(profit_list), w, profit_list, weight_list, memo)
#     print(f"Duration: {datetime.now() - start_time} (with memoization    ). KnapSack for {w} : {knap_sack}")
#
#
# def test_knap_sack_with_all_ways(w: int, profit_list: List[int], weight_list: List[int]):
#     test_knap_sack_recursive(w, profit_list, weight_list)
#     test_knap_sack_with_memoization(w, profit_list, weight_list)
#
#
# if __name__ == "__main__":
#     test_knap_sack_with_all_ways(50, [60, 100, 120, 40, 20, 30], [10, 20, 30, 15, 5, 12])
#     test_knap_sack_with_all_ways(4, [10, 20, 30], [1, 2, 3])
#     test_knap_sack_with_all_ways(50, [60, 100, 120], [10, 20, 30])
#     test_knap_sack_with_all_ways(500, [i * 10 for i in range(1, 25)], [i for i in range(1, 25)])
