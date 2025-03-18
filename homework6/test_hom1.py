from datetime import datetime

import pytest

from hom1 import knap_sack_recursive, knap_sack_with_memoization, knap_sack_with_tabulation

test_data = {
    "test1": {
        "profit_list": [60, 100, 120, 40, 20, 30],
        "weight_list": [10, 20, 30, 15, 5, 12],
        "capacity": 50,
        "expected_result": 220
    },
    "test2": {
        "profit_list": [10, 20, 30],
        "weight_list": [1, 2, 3],
        "capacity": 4,
        "expected_result": 40
    },
    "test3": {
        "profit_list": [60, 100, 120],
        "weight_list": [10, 20, 30],
        "capacity": 50,
        "expected_result": 220
    },
    "test4": {
        "profit_list": [i * 10 for i in range(1, 25)],
        "weight_list": [i for i in range(1, 25)],
        "capacity": 500,
        "expected_result": 3000
    },
    "test5": {
        "profit_list": [i * 10 for i in range(1, 12)],
        "weight_list": [i for i in range(1, 12)],
        "capacity": 160,
        "expected_result": 660
    }
}


@pytest.mark.parametrize(
    "test_case",
    list(test_data.keys())
)
def test_knap_sack_recursive(test_case):
    data = test_data[test_case]

    result = knap_sack_recursive(len(data["profit_list"]), data["capacity"], data["profit_list"], data["weight_list"])
    assert result == data["expected_result"]


@pytest.mark.parametrize(
    "test_case",
    list(test_data.keys())
)
def test_knap_sack_with_memoization(test_case):
    data = test_data[test_case]

    memo = [[-1 for _ in range(data["capacity"] + 1)] for _ in range(len(data["profit_list"]) + 1)]
    result = knap_sack_with_memoization(len(data["profit_list"]), data["capacity"], data["profit_list"],
                                        data["weight_list"], memo)
    assert result == data["expected_result"]


@pytest.mark.parametrize(
    "test_case",
    list(test_data.keys())
)
def test_knap_sack_with_tabulation(test_case):
    data = test_data[test_case]

    result = knap_sack_with_tabulation(len(data["profit_list"]), data["capacity"], data["profit_list"],
                                       data["weight_list"])
    assert result == data["expected_result"]


def test_knap_sack_time():
    data = test_data["test4"]
    start_time = datetime.now()
    knap_sack_recursive(len(data["profit_list"]), data["capacity"], data["profit_list"], data["weight_list"])
    duration_recursive = datetime.now() - start_time

    start_time = datetime.now()
    memo_4 = [[-1 for _ in range(data["capacity"] + 1)] for _ in range(len(data["profit_list"]) + 1)]
    knap_sack_with_memoization(len(data["profit_list"]), data["capacity"], data["profit_list"], data["weight_list"],
                               memo_4)
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
