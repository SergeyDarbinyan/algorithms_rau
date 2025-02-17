# 1. Տրված է n չափսի arr սորտավորված զանգվածը: Գտնել arr-ի այն տարրերի քանակը, որոնք փոքր են կամ հավասար value-ից:
#    Ակնկալվող ժամանակի բարդությունը O (log N)։
#    Օրինակ 1
#    Մտք՝ arr = [1, 3, 4, 4, 6] value = 4
#    Ելք՝ 4
#    Օրինակ 2
#    Մտք՝ arr = [1, 2, 4, 6] value = 3
#    Ելք՝ 2

def find_index_of_value(arr, value, start, end):
    if start > end:
        return -1

    arr_mid = (start + end) // 2
    if value == arr[arr_mid]:
        return arr_mid
    elif value > arr[arr_mid]:
        return find_index_of_value(arr, value, arr_mid + 1, end)
    else:
        return find_index_of_value(arr, value, start, arr_mid - 1)


def find_value_count(arr, value):
    index = find_index_of_value(arr, value, 0, len(arr) - 1)
    if index == -1:
        return 0

    # first solution
    tmp_val = arr[0]
    count_uniq = 1
    for val in arr[1:index + 1]:
        if val != tmp_val:
            count_uniq += 1
        tmp_val = val

    # second solution
    # unique_values = set(arr[:index + 1])
    # count_uniq = len(unique_values)
    return count_uniq


if __name__ == "__main__":
    arr_list = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10, 11, 12, 13]
    count = find_value_count(arr_list, 2)
    print(count)
