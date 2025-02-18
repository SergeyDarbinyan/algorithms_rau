# Իրականացնել QuickSort ալգորիթմը:
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


if __name__ == "__main__":
    arr_list: List[int] = [2, 1, 5, 3, 9, 7, 0, 3]
    quick_sort(arr_list, 0, len(arr_list) - 1)
    print(arr_list)
