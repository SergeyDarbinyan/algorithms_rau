# 1. Տրված է ամբողջ ոչ բացասական թվեր պարունակող arr զանգվածը։
# Հաշվել բոլոր (i, j) զույգերը (0 <= i < j < arr.length), որոնց համար arr[i] և arr[j] թվերն անագրամ են։
# Երկու թվեր համարվում են անագրամ, եթե նրանք պարունակում են նույն քանակությամբ թվանշաններ,
# և մի թվից կարելի է ստանալ մյուս կատարելով թվանշանների տեղափոխթյուն։
# Օրինակ՝ 53295 և 35592 թվերը անագրամ են, իսկ 345 և 375 ոչ։ 990 և 99 նույնպես անագրամ չեն։
# Մուտք
# Տրված է arr զանգվածը, 1 ≤ arr.length ≤ 105, 0 ≤ arr[i] ≤ 109 :
# Ելք
# Բոլոր i և j զույգերի քանակը, այնպես որ arr[i] և arr[j] անագրամ են։
# Օրինակ
# Մտք
# arr = [78, 43, 872, 228, 34, 278, 872]
# Ելք
# 4
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


def swap(arr: List, i: int, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: List[int], low: int, high: int):
    if low < high:
        piv_index: int = partitioning(arr, low, high)

        quick_sort(arr, low, piv_index - 1)
        quick_sort(arr, piv_index + 1, high)


def is_anagram(num1: int, num2: int) -> bool:
    if num1 == num2:
        return False
    num1_digits: List[int] = []
    num2_digits: List[int] = []
    while num1 > 0:
        num1_digits.append(num1 % 10)
        num1 = num1 // 10
    while num2 > 0:
        num2_digits.append(num2 % 10)
        num2 = num2 // 10

    if len(num1_digits) != len(num2_digits):
        return False

    quick_sort(num1_digits, 0, len(num1_digits) - 1)
    quick_sort(num2_digits, 0, len(num2_digits) - 1)
    for i in range(0, len(num1_digits) - 1):
        if num1_digits[i] != num2_digits[i]:
            return False
    return True


def count_anagram_numbers(arr: List[int]) -> int:
    quick_sort(arr, 0, len(arr) - 1)
    count: int = 0
    for i in range(0, len(arr) - 1):
        # for j in range(i+1, len(arr) - 1):
            # if is_anagram(arr[i], arr[j]):
            #     print([arr[i], arr[j]])
            #     count += 1
        if arr[i + 1] and is_anagram(arr[i], arr[i + 1]):
            count += 2
    return count


def test_count_anagram_numbers():
    # Test case 1: Multiple anagram pairs
    arr = [78, 43, 872, 228, 34, 278, 872]
    result = count_anagram_numbers(arr)
    print(f"Test case 1: {result}")  # Expected: 4

    # Test case 2: No anagram pairs
    arr = [12, 34, 56, 78]
    result = count_anagram_numbers(arr)
    print(f"Test case 2: {result}")  # Expected: 0

    # Test case 3: Only one number in the array
    arr = [123]
    result = count_anagram_numbers(arr)
    print(f"Test case 3: {result}")  # Expected: 0 (no pairs possible)

    # Test case 4: Array with duplicates but not anagrams
    arr = [123, 321, 456, 654, 111]
    result = count_anagram_numbers(arr)
    print(f"Test case 4: {result}")  # Expected: 2 (123 and 321 are anagrams, 456 and 654 are anagrams)

    # Test case 5: Array with numbers of different digit lengths
    arr = [12, 123, 1234, 4321]
    result = count_anagram_numbers(arr)
    print(f"Test case 5: {result}")  # Expected: 0 (no anagrams since they have different digit lengths)

    # Test case 6: Array with repeated anagrams
    arr = [123, 132, 213, 321, 231]
    result = count_anagram_numbers(arr)
    print(f"Test case 6: {result}")  # Expected: 10 (5 pairs of anagrams)


if __name__ == "__main__":
    test_count_anagram_numbers()

if __name__ == "__main__":
    arr_list: List[int] = [78, 43, 872, 228, 34, 278, 872]
    count_numbers: int = count_anagram_numbers(arr_list)
    print(count_numbers)
