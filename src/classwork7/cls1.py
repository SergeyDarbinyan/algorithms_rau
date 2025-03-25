# SumSet sum problem
from datetime import datetime
from typing import List


def sum_set_recursive(arr: List[int], suma: int, n: int) -> bool:
    if suma == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] > suma:
        return sum_set_recursive(arr, suma, n - 1)

    return sum_set_recursive(arr, suma, n - 1) or sum_set_recursive(arr, suma - arr[n - 1], n - 1)


def sum_set_with_memoization(arr: List[int], suma: int, n: int, memo: List[List[int]]) -> bool:
    if suma == 0:
        return True
    if n == 0:
        return False
    if memo[n][suma] != -1:
        return bool(memo[n][suma])
    if arr[n - 1] > suma:
        memo[n][suma] = sum_set_with_memoization(arr, suma, n - 1, memo)
    else:
        memo[n][suma] = (
                sum_set_with_memoization(arr, suma, n - 1, memo) or
                sum_set_with_memoization(arr, suma - arr[n - 1], n - 1, memo))

    return bool(memo[n][suma])


def sum_set_with_tabulation(arr: List[int], suma: int) -> bool:
    n: int = len(arr)
    dp: List[List[bool]] = [[False for _ in range(suma + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, suma + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][suma]


def my_test_sum_set_recursive(arr: List[int], suma: int):
    start_time: datetime = datetime.now()
    sum_set: int = sum_set_recursive(arr, suma, len(arr))
    print(f"Duration: {datetime.now() - start_time} (without optimization). SumSet for {suma} sum in {arr} : {sum_set}")


def my_test_sum_set_with_memoization(arr: List[int], suma: int):
    start_time: datetime = datetime.now()
    memo: List[List[int]] = [[-1 for _ in range(suma + 1)] for _ in range(len(arr) + 1)]
    sum_set: int = sum_set_with_memoization(arr, suma, len(arr), memo)
    print(f"Duration: {datetime.now() - start_time} (without optimization). SumSet for {suma} sum in {arr} : {sum_set}")


def my_test_sum_set_with_tabulation(arr: List[int], suma: int):
    start_time: datetime = datetime.now()
    sum_set: int = sum_set_with_tabulation(arr, suma)
    print(f"Duration: {datetime.now() - start_time} (without optimization). SumSet for {suma} sum in {arr} : {sum_set}")


def my_test_sum_set_with_all_ways(arr: List[int], suma: int):
    my_test_sum_set_recursive(arr, suma)
    my_test_sum_set_with_memoization(arr, suma)
    my_test_sum_set_with_tabulation(arr, suma)


if __name__ == "__main__":
    my_test_sum_set_with_all_ways([10], 10)
    my_test_sum_set_with_all_ways([10, 20, 30], 15)
    my_test_sum_set_with_all_ways([1, 2, 3, 4, 5, 6], 15)
    my_test_sum_set_with_all_ways([1, 2, 3, 4, 5], 20)
    my_test_sum_set_with_all_ways(list(range(1, 25)), 500)
