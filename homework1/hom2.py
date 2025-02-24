# 2. Տրված է n չափսի arr սորտավորված զանգվածը և value : Գտնել value-ի սկզբնական և վերջնական ինդեքսները arr-ում:
#    Վերադարձվում է 2 երկարությամբ զանգված, այնպես որ առաջին էլեմենտը լինի value -ի սկզբական ինդեքսը զանգվածում, երկրորդ էլեմենտը` վերջնական։ Եթե այդպիսի տարր չկա վերադարձնել [-1, -1]:
#    Ակնկալվող ժամանակի բարդություն O (log N)։
#    Օրինակ 1
#    Մտք՝ arr = [1, 3, 4, 4, 6] value = 4
#    Ելք՝ [2, 3]
#    Օրինակ 2
#    Մտք՝ arr = [1, 2, 4, 6] value = 3
#    Ելք՝ [-1, -1]
#    Օրինակ 3
#    Մտք՝ arr = [1, 1, 1, 1] value = 1
#    Ելք՝ [0, 3]
from typing import List


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


def find_occurrence(arr: List[int], k: int) -> List[int]:
    left_index: int = find_left_occurrence(arr, k, 0, len(arr) - 1)
    right_index: int = find_right_occurrence(arr, k, 0, len(arr) - 1)

    if left_index == -1:
        return [-1, -1]

    return [left_index, right_index]


def test_find_occurrence():
    arr = [1, 3, 4, 4, 6]
    result = find_occurrence(arr, 4)
    print(f"Test case 1 (value 4): {result}")  # Expected: [2, 3]

    arr = [1, 2, 4, 6]
    result = find_occurrence(arr, 3)
    print(f"Test case 2 (value 3): {result}")  # Expected: [-1, -1]

    arr = [1, 2, 4, 6]
    result = find_occurrence(arr, 4)
    print(f"Test case 3 (value 4): {result}")  # Expected: [2, 2]

    arr = [1, 1, 1, 1]
    result = find_occurrence(arr, 1)
    print(f"Test case 4 (value 1): {result}")  # Expected: [0, 3]

    arr = [1, 3, 4, 5, 7, 7, 7, 7]
    result = find_occurrence(arr, 7)
    print(f"Test case 5 (value 7): {result}")  # Expected: [4, 7]

    arr = []
    result = find_occurrence(arr, 5)
    print(f"Test case 6 (empty array, value 5): {result}")  # Expected: [-1, -1]

    arr = [3, 3, 3, 4, 5]
    result = find_occurrence(arr, 3)
    print(f"Test case 7 (value 3 at the beginning): {result}")  # Expected: [0, 2]

    arr = [1, 2, 3, 4, 5, 5]
    result = find_occurrence(arr, 5)
    print(f"Test case 8 (value 5 at the end): {result}")  # Expected: [4, 5]


if __name__ == "__main__":
    test_find_occurrence()
