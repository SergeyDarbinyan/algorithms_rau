# 1. Տրված են arr բանալիների տեսակավորված զանգվածն  k բանալին։
#   a. Նկարագրել (բառերով) arr զանգվածում k բանալու հանդիպմների քանակի որոշման (lgn) բարդության ալգորիթմը։
#   b. Իրականացնել առաջարկված ալգորիթմը։

def find_left_occurrence(arr, k, start, end):
    if start > end:
        return -1

    mid = (end - start) // 2 + start

    if arr[mid] == k and (mid == 0 or arr[mid - 1] < k):
        return mid

    if arr[mid] < k:
        start = mid + 1
        return find_left_occurrence(arr, k, start, end)
    else:
        end = mid - 1
        return find_left_occurrence(arr, k, start, end)


def find_right_occurrence(arr, k, start, end):
    if start > end:
        return -1

    mid = (end - start) // 2 + start

    if arr[mid] == k and (mid == len(arr) - 1 or arr[mid + 1] > k):
        return mid

    if arr[mid] > k:
        end = mid - 1
        return find_right_occurrence(arr, k, start, end)
    else:
        start = mid + 1
        return find_right_occurrence(arr, k, start, end)


def find_occurrence_(arr, k):
    left_index = find_left_occurrence(arr, k, 0, len(arr) - 1)
    right_index = find_right_occurrence(arr, k, 0, len(arr) - 1)

    if left_index == -1:
        return f"{k} not found in the list"

    return right_index - left_index + 1


if __name__ == "__main__":
    arr_list = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 12, 13]
    count = find_occurrence_(arr_list, 8)
    print(count)
