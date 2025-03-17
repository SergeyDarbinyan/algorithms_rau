# 1. Տրված են arr բանալիների տեսակավորված զանգվածն  k բանալին։
#   a. Նկարագրել (բառերով) arr զանգվածում k բանալու հանդիպմների քանակի որոշման (lgn) բարդության ալգորիթմը։
#   b. Իրականացնել առաջարկված ալգորիթմը։
from datetime import datetime
from typing import List, Union


def find_left_occurrence(arr: List[int], k: int, start: int, end: int) -> int:
    if start > end:
        return -1

    mid: int = (end - start) // 2 + start

    if arr[mid] == k and (mid == 0 or arr[mid - 1] < k):
        return mid

    if arr[mid] < k:
        start = mid + 1
        return find_left_occurrence(arr, k, start, end)
    else:
        end = mid - 1
        return find_left_occurrence(arr, k, start, end)


def find_right_occurrence(arr: List[int], k: int, start: int, end: int) -> int:
    if start > end:
        return -1

    mid: int = (end - start) // 2 + start

    if arr[mid] == k and (mid == len(arr) - 1 or arr[mid + 1] > k):
        return mid

    if arr[mid] > k:
        end = mid - 1
        return find_right_occurrence(arr, k, start, end)
    else:
        start = mid + 1
        return find_right_occurrence(arr, k, start, end)


def find_occurrence_(arr: List[int], k: int) -> Union[str, int]:
    left_index: int = find_left_occurrence(arr, k, 0, len(arr) - 1)
    right_index: int = find_right_occurrence(arr, k, 0, len(arr) - 1)

    if left_index == -1:
        return f"{k} not found in the list"

    return right_index - left_index + 1


def my_test_find_occurrence():
    arr_list: List[int] = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 12, 13]

    start_time = datetime.now()
    result = find_occurrence_(arr_list, 100)
    print(
        f"Duration-{datetime.now() - start_time}: Test case 1 (100 not in list): {result}")  # Expected: "100 not found in the list"

    start_time = datetime.now()
    result = find_occurrence_(arr_list, 12)
    print(f"Duration-{datetime.now() - start_time}: Test case 2 (12 appears once): {result}")  # Expected: 1

    start_time = datetime.now()
    result = find_occurrence_(arr_list, 7)
    print(f"Duration-{datetime.now() - start_time}: Test case 3 (7 appears multiple times): {result}")  # Expected: 4

    start_time = datetime.now()
    result = find_occurrence_(arr_list, 1)
    print(f"Duration-{datetime.now() - start_time}: Test case 5 (1 at the start): {result}")  # Expected: 1

    start_time = datetime.now()
    result = find_occurrence_(arr_list, 13)
    print(f"Duration-{datetime.now() - start_time}: Test case 6 (13 at the end): {result}")  # Expected: 1

    start_time = datetime.now()
    empty_list: List[int] = []
    result = find_occurrence_(empty_list, 1)
    print(
        f"Duration-{datetime.now() - start_time}: Test case 4 (Empty list): {result}")  # Expected: "1 not found in the list"


if __name__ == "__main__":
    my_test_find_occurrence()
