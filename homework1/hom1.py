# 1. Տրված է n չափսի arr սորտավորված զանգվածը: Գտնել arr-ի այն տարրերի քանակը, որոնք փոքր են կամ հավասար value-ից:
#    Ակնկալվող ժամանակի բարդությունը O (log N)։
#    Օրինակ 1
#    Մտք՝ arr = [1, 3, 4, 4, 6] value = 4
#    Ելք՝ 4
#    Օրինակ 2
#    Մտք՝ arr = [1, 2, 4, 6] value = 3
#    Ելք՝ 2
from typing import List


def find_index_of_value(arr: List[int], value: int, start: int, end: int) -> int:
    mid: int = (end - start) // 2 + start
    if start > end:
        return mid

    if arr[mid] == value and (mid == len(arr) - 1 or arr[mid + 1] > value):
        return mid

    if arr[mid] > value:
        end = mid - 1
        return find_index_of_value(arr, value, start, end)
    else:
        start = mid + 1
        return find_index_of_value(arr, value, start, end)

    # Its for another problem, for counting uniq values <= value
    # if start > end:
    #     return arr_mid
    #
    # arr_mid: int = (start + end) // 2
    # if value == arr[arr_mid]:
    #     return arr_mid
    # elif value > arr[arr_mid]:
    #     return find_index_of_value(arr, value, arr_mid + 1, end)
    # else:
    #     return find_index_of_value(arr, value, start, arr_mid - 1)


def find_value_count(arr: List[int], value: int) -> int:
    index: int = find_index_of_value(arr, value, 0, len(arr) - 1)
    if index == -1:
        return 0

    # Its for another problem, for counting uniq values <= value

    # first solution
    # tmp_val: int = arr[0]
    # count_uniq: int = 1
    # for val in arr[1:index + 1]:
    #     if val != tmp_val:
    #         count_uniq += 1
    #     tmp_val = val

    # second solution
    # unique_values: set = set(arr[:index + 1])
    # count_uniq: int = len(unique_values)

    count_le_numbers = len(arr[:index + 1])
    return count_le_numbers


def test_find_value_count():
    arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 12, 13]

    result = find_value_count(arr, 4)
    print(f"Test case 1 (value 4): {result}")  # Expected: 4 (1, 2, 3, 3)

    result = find_value_count(arr, 14)
    print(f"Test case 3 (value 14): {result}")  # Expected: 18 (since all elements are less than 14)

    result = find_value_count(arr, 13)
    print(f"Test case 4 (value 13): {result}")  # Expected: 18 (since all elements less than or equal to 13 are counted)

    result = find_value_count(arr, 7)
    print(f"Test case 5 (value 7): {result}")  # Expected: 12 (1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7)

    result = find_value_count([], 4)
    print(f"Test case 6 (Empty list, value 4): {result}")  # Expected: 0 (no elements to count)

    result = find_value_count([3], 4)
    print(f"Test case 7 (Array with one element, value 4): {result}")  # Expected: 1 (value 3 is less than 4)

    result = find_value_count([5], 4)
    print(f"Test case 8 (Array with one element, value 4): {result}")  # Expected: 0 (value 5 is greater than 4)


if __name__ == "__main__":
    test_find_value_count()
