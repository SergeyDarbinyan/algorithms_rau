# 1. Տրված է բնական թվերի numbers բազմությունը և Q բնական թիվը։ Անհրաժեշտ է գտնել նվազագույն ենթաբազմությունը
# (ամենաքիչ տարրեր պարունակող), որի տարրերի գումարը հավասար է Q թվին։
# Օրինակ 1
# Մուտք՝ numbers = [3, 1, 4, 8, 6], Q = 9
# Ելք՝ [3, 6] (կամ [1, 8])
# Օրինակ 2
# Մուտք՝ numbers = [3, 1, 4, 8, 6, 1, 9], Q = 9
# Ելք՝ [9]
from datetime import datetime
from typing import List


def sum_set_min_elements_recursive(arr: List[int], suma: int, index: int, curr: List[int], result: List[int]):
    if index >= len(arr):
        if suma == 0:
            if not result or len(curr) < len(result):
                result[:] = curr[:]
        return

    curr.append(arr[index])
    sum_set_min_elements_recursive(arr, suma - arr[index], index + 1, curr, result)

    curr.pop()
    sum_set_min_elements_recursive(arr, suma, index + 1, curr, result)


def my_test_sum_set_min_elements_recursive(arr: List[int], suma: int):
    result: List[int] = []
    start_time: datetime = datetime.now()
    sum_set_min_elements_recursive(arr, suma, 0, [], result)
    print(
        f"Duration: {datetime.now() - start_time} (without optimization). SumSet with minimal elements for {suma} sum in {arr} : {result}")


def my_test_sum_set_min_elements_with_all_ways(arr: List[int], suma: int):
    my_test_sum_set_min_elements_recursive(arr, suma)


if __name__ == "__main__":
    my_test_sum_set_min_elements_with_all_ways([3, 1, 4, 8, 6], 9)
    my_test_sum_set_min_elements_with_all_ways([3, 1, 4, 8, 6, 1, 9], 9)
    my_test_sum_set_min_elements_with_all_ways([1, 2, 3, 4, 5, 6], 15)
    my_test_sum_set_min_elements_with_all_ways([1, 2, 3, 4, 5], 20)
    my_test_sum_set_min_elements_with_all_ways(list(range(1, 25)), 300)
    my_test_sum_set_min_elements_with_all_ways([5, 10, 15], 30)
    my_test_sum_set_min_elements_with_all_ways([1, 3, 5, 7, 9, 11], 12)
    my_test_sum_set_min_elements_with_all_ways([100, 200, 300, 400, 500], 600)
