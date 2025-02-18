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


if __name__ == "__main__":
    arr_list: List[int] = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 12, 13]
    k_occurrence: List[int] = find_occurrence(arr_list, 7)
    print(k_occurrence)
