# KnapSack 0/1

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


def knap_sack_with_tabulation(n, w, profit_list: List[int], weight_list: List[int]) -> int:
    dp: List[List[int]] = [[0 for _ in range(w + 1)] for _ in range(len(profit_list) + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weight_list[i - 1] <= j:
                dp[i][j] = max(profit_list[i - 1] + dp[i - 1][j - weight_list[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]


def my_test_knap_sack_recursive(w: int, profit_list: List[int], weight_list: List[int]):
    start_time: datetime = datetime.now()
    knap_sack: int = knap_sack_recursive(len(profit_list), w, profit_list, weight_list)
    print(f"Duration: {datetime.now() - start_time} (without optimization). KnapSack for {w} : {knap_sack}")


def my_test_knap_sack_with_memoization(w: int, profit_list: List[int], weight_list: List[int]):
    start_time: datetime = datetime.now()
    memo: List[List[int]] = [[-1 for _ in range(w + 1)] for _ in range(len(profit_list) + 1)]
    knap_sack: int = knap_sack_with_memoization(len(profit_list), w, profit_list, weight_list, memo)
    print(f"Duration: {datetime.now() - start_time} (with memoization    ). KnapSack for {w} : {knap_sack}")


def my_test_knap_sack_with_tabulation(w: int, profit_list: List[int], weight_list: List[int]):
    start_time: datetime = datetime.now()
    knap_sack: int = knap_sack_with_tabulation(len(profit_list), w, profit_list, weight_list)
    print(f"Duration: {datetime.now() - start_time} (with tabulation     ). KnapSack for {w} : {knap_sack}")


def my_test_knap_sack_with_all_ways(w: int, profit_list: List[int], weight_list: List[int]):
    my_test_knap_sack_recursive(w, profit_list, weight_list)
    my_test_knap_sack_with_memoization(w, profit_list, weight_list)
    my_test_knap_sack_with_tabulation(w, profit_list, weight_list)


if __name__ == "__main__":
    my_test_knap_sack_with_all_ways(50, [60, 100, 120, 40, 20, 30], [10, 20, 30, 15, 5, 12])
    my_test_knap_sack_with_all_ways(4, [10, 20, 30], [1, 2, 3])
    my_test_knap_sack_with_all_ways(50, [60, 100, 120], [10, 20, 30])
    my_test_knap_sack_with_all_ways(500, [i * 10 for i in range(1, 25)], [i for i in range(1, 25)])
