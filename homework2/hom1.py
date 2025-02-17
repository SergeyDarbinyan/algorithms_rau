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


def partitioning(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        piv_index = partitioning(arr, low, high)

        quick_sort(arr, low, piv_index - 1)
        quick_sort(arr, piv_index + 1, high)


def is_anagram(num1, num2):
    if num1==num2:
        return False
    num1_digits = []
    num2_digits = []
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

def count_anagram_numbers(arr):
    quick_sort(arr, 0, len(arr)-1)
    count = 0
    for i in range(0, len(arr) - 1):
        if arr[i+1] and is_anagram(arr[i], arr[i+1]):
            count+=2
    return count

if __name__ == "__main__":
    arr_list = [78, 43, 872, 228, 34, 278, 872]
    res = count_anagram_numbers(arr_list)
    print(res)
