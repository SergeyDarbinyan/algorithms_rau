# 3. Տրված է բնական թվերի numbers բազմությունը և Q բնական թիվը։ Անհրաժեշտ է գտնել բոլոր այն ենթաբազմությունները,
# որոնց տարրերի գումարը հավասար է Q թվին։
# Օրինակ 1
# Մուտք՝ numbers = [3, 1, 4, 8, 6], Q = 8
# Ելք՝ [[3, 1, 4], [8]]
# Օրինակ 2
# Մուտք՝ numbers = [1, 1, 1], Q = 2
# Ելք՝ [[1, 1], [1, 1], [1, 1]]
from datetime import datetime
from typing import List


def sum_set_all_recursive(arr: List[int], suma: int, index: int, curr: List[int], result: List[List[int]]):
    if index >= len(arr):
        if suma == 0:
            result.append(curr[:])
        return

    curr.append(arr[index])
    sum_set_all_recursive(arr, suma - arr[index], index + 1, curr, result)

    curr.pop()
    sum_set_all_recursive(arr, suma, index + 1, curr, result)


def sum_set_all_with_tabulation(arr: List[int], suma: int) -> List[int]:
    dp = [[] for _ in range(suma + 1)]
    dp[0].append([])
    for num in arr:
        for sum_value in range(suma, num - 1, -1):
            for subset in dp[sum_value - num]:
                dp[sum_value].append(subset + [num])

    return dp[suma]


def my_test_sum_set_all_recursive(arr: List[int], suma: int):
    result: List[List[int]] = []
    start_time: datetime = datetime.now()
    sum_set_all_recursive(arr, suma, 0, [], result)
    print(
        f"Duration: {datetime.now() - start_time} (without optimization). SumSet with minimal elements for {suma} sum in {arr} : {result}")


def my_test_sum_set_all_with_tabulation(arr: List[int], suma: int):
    start_time: datetime = datetime.now()
    result = sum_set_all_with_tabulation(arr, suma)
    print(
        f"Duration: {datetime.now() - start_time} (without tabulation  ). SumSet with minimal elements for {suma} sum in {arr} : {result}")


def my_test_sum_set_all_with_all_ways(arr: List[int], suma: int):
    my_test_sum_set_all_recursive(arr, suma)
    my_test_sum_set_all_with_tabulation(arr, suma)


if __name__ == "__main__":
    my_test_sum_set_all_with_all_ways([3, 1, 4, 8, 6], 9)
    my_test_sum_set_all_with_all_ways([3, 1, 4, 8, 6, 1, 9], 9)
    my_test_sum_set_all_with_all_ways([3, 1, 4, 8, 6], 8)
    my_test_sum_set_all_with_all_ways([1, 1, 1], 2)
    my_test_sum_set_all_with_all_ways([1, 2, 3, 4, 5, 6], 15)
    my_test_sum_set_all_with_all_ways(list(range(1, 25)), 300)
    my_test_sum_set_all_with_all_ways([100, 200, 300, 400, 500], 600)
