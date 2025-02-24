# Իրականացնել QuickSort ալգորիթմը:
from datetime import datetime
from typing import List


def partitioning(arr: List[int], low: int, high: int) -> int:
    pivot: int = arr[high]
    i: int = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1


def swap(arr: List[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: List[int], low: int, high: int):
    if low < high:
        piv_index: int = partitioning(arr, low, high)

        quick_sort(arr, low, piv_index - 1)
        quick_sort(arr, piv_index + 1, high)


def test_quick_sort():
    arr = [2, 1, 5, 3, 9, 7, 0, 3]
    start_time = datetime.now()
    quick_sort(arr, 0, len(arr) - 1)
    print(
        f"Duration-{datetime.now() - start_time}: Test case 1 (Random unordered list): {arr}")  # Expected: [0, 1, 2, 3, 3, 5, 7, 9]

    arr = [1, 2, 3, 4, 5, 6]
    start_time = datetime.now()
    quick_sort(arr, 0, len(arr) - 1)
    print(
        f"Duration-{datetime.now() - start_time}: Test case 2 (Already sorted list): {arr}")  # Expected: [1, 2, 3, 4, 5, 6]

    arr = [4, 2, 5, 3, 2, 4, 2]
    start_time = datetime.now()
    quick_sort(arr, 0, len(arr) - 1)
    print(
        f"Duration-{datetime.now() - start_time}: Test case 3 (List with duplicates): {arr}")  # Expected: [2, 2, 2, 3, 4, 4, 5]

    arr = []
    start_time = datetime.now()
    quick_sort(arr, 0, len(arr) - 1)
    print(f"Duration-{datetime.now() - start_time}: Test case 4 (Empty list): {arr}")  # Expected: []

    arr = [10]
    start_time = datetime.now()
    quick_sort(arr, 0, len(arr) - 1)
    print(f"Duration-{datetime.now() - start_time}: Test case 5 (Single element list): {arr}")  # Expected: [10]

    arr = [7, 7, 7, 7, 7]
    start_time = datetime.now()
    quick_sort(arr, 0, len(arr) - 1)
    print(
        f"Duration-{datetime.now() - start_time}: Test case 6 (List with all identical elements): {arr}")  # Expected: [7, 7, 7, 7, 7]


if __name__ == "__main__":
    test_quick_sort()
