import pytest
from datetime import datetime
from hom1 import knap_sack_recursive, knap_sack_with_memoization

profit_list_1 = [60, 100, 120, 40, 20, 30]
weight_list_1 = [10, 20, 30, 15, 5, 12]
capacity_1 = 50
expected_result_1 = 220

profit_list_2 = [10, 20, 30]
weight_list_2 = [1, 2, 3]
capacity_2 = 4
expected_result_2 = 40

profit_list_3 = [60, 100, 120]
weight_list_3 = [10, 20, 30]
capacity_3 = 50
expected_result_3 = 220

profit_list_4 = [i * 10 for i in range(1, 25)]
weight_list_4 = [i for i in range(1, 25)]
capacity_4 = 500
expected_result_4 = 3000


def test_knap_sack_recursive():
    # Test 1
    result_1 = knap_sack_recursive(len(profit_list_1), capacity_1, profit_list_1, weight_list_1)
    assert result_1 == expected_result_1

    # Test 2
    result_2 = knap_sack_recursive(len(profit_list_2), capacity_2, profit_list_2, weight_list_2)
    assert result_2 == expected_result_2

    # Test 3
    result_3 = knap_sack_recursive(len(profit_list_3), capacity_3, profit_list_3, weight_list_3)
    assert result_3 == expected_result_3


def test_knap_sack_with_memoization():
    memo_1 = [[-1 for _ in range(capacity_1 + 1)] for _ in range(len(profit_list_1) + 1)]
    result_1 = knap_sack_with_memoization(len(profit_list_1), capacity_1, profit_list_1, weight_list_1, memo_1)
    assert result_1 == expected_result_1

    memo_2 = [[-1 for _ in range(capacity_2 + 1)] for _ in range(len(profit_list_2) + 1)]
    result_2 = knap_sack_with_memoization(len(profit_list_2), capacity_2, profit_list_2, weight_list_2, memo_2)
    assert result_2 == expected_result_2

    memo_3 = [[-1 for _ in range(capacity_3 + 1)] for _ in range(len(profit_list_3) + 1)]
    result_3 = knap_sack_with_memoization(len(profit_list_3), capacity_3, profit_list_3, weight_list_3, memo_3)
    assert result_3 == expected_result_3


def test_knap_sack_time():
    start_time = datetime.now()
    knap_sack_recursive(len(profit_list_4), capacity_4, profit_list_4, weight_list_4)
    duration_recursive = datetime.now() - start_time

    start_time = datetime.now()
    memo_4 = [[-1 for _ in range(capacity_4 + 1)] for _ in range(len(profit_list_4) + 1)]
    knap_sack_with_memoization(len(profit_list_4), capacity_4, profit_list_4, weight_list_4, memo_4)
    duration_memoization = datetime.now() - start_time

    print(f"\nRecursive Duration: {duration_recursive}")
    print(f"Memoization Duration: {duration_memoization}")


if __name__ == "__main__":
    pytest.main()

# class TestKnapsack(unittest.TestCase):
#
#     def setUp(self):
#         self.profit_list_1 = [60, 100, 120, 40, 20, 30]
#         self.weight_list_1 = [10, 20, 30, 15, 5, 12]
#         self.capacity_1 = 50
#         self.expected_result_1 = 220
#
#         self.profit_list_2 = [10, 20, 30]
#         self.weight_list_2 = [1, 2, 3]
#         self.capacity_2 = 4
#         self.expected_result_2 = 40
#
#         self.profit_list_3 = [60, 100, 120]
#         self.weight_list_3 = [10, 20, 30]
#         self.capacity_3 = 50
#         self.expected_result_3 = 220
#
#         self.profit_list_4 = [i * 10 for i in range(1, 25)]
#         self.weight_list_4 = [i for i in range(1, 25)]
#         self.capacity_4 = 500
#         self.expected_result_4 = 3000
#
#     def test_knap_sack_recursive(self):
#         result_1 = knap_sack_recursive(len(self.profit_list_1), self.capacity_1, self.profit_list_1,
#                                        self.weight_list_1)
#         self.assertEqual(result_1, self.expected_result_1)
#
#         result_2 = knap_sack_recursive(len(self.profit_list_2), self.capacity_2, self.profit_list_2,
#                                        self.weight_list_2)
#         self.assertEqual(result_2, self.expected_result_2)
#
#         result_3 = knap_sack_recursive(len(self.profit_list_3), self.capacity_3, self.profit_list_3,
#                                        self.weight_list_3)
#         self.assertEqual(result_3, self.expected_result_3)
#
#     def test_knap_sack_with_memoization(self):
#         memo_1 = [[-1 for _ in range(self.capacity_1 + 1)] for _ in range(len(self.profit_list_1) + 1)]
#         result_1 = knap_sack_with_memoization(len(self.profit_list_1), self.capacity_1, self.profit_list_1,
#                                               self.weight_list_1, memo_1)
#         self.assertEqual(result_1, self.expected_result_1)
#
#         memo_2 = [[-1 for _ in range(self.capacity_2 + 1)] for _ in range(len(self.profit_list_2) + 1)]
#         result_2 = knap_sack_with_memoization(len(self.profit_list_2), self.capacity_2, self.profit_list_2,
#                                               self.weight_list_2, memo_2)
#         self.assertEqual(result_2, self.expected_result_2)
#
#         memo_3 = [[-1 for _ in range(self.capacity_3 + 1)] for _ in range(len(self.profit_list_3) + 1)]
#         result_3 = knap_sack_with_memoization(len(self.profit_list_3), self.capacity_3, self.profit_list_3,
#                                               self.weight_list_3, memo_3)
#         self.assertEqual(result_3, self.expected_result_3)
#
#     def test_knap_sack_time(self):
#         start_time = datetime.now()
#         knap_sack_recursive(len(self.profit_list_4), self.capacity_4, self.profit_list_4, self.weight_list_4)
#         duration_recursive = datetime.now() - start_time
#
#         start_time = datetime.now()
#         memo_4 = [[-1 for _ in range(self.capacity_4 + 1)] for _ in range(len(self.profit_list_4) + 1)]
#         knap_sack_with_memoization(len(self.profit_list_4), self.capacity_4, self.profit_list_4, self.weight_list_4,
#                                    memo_4)
#         duration_memoization = datetime.now() - start_time
#
#         print(f"Recursive Duration: {duration_recursive}")
#         print(f"Memoization Duration: {duration_memoization}")
#
#
# if __name__ == "__main__":
#     unittest.main()
