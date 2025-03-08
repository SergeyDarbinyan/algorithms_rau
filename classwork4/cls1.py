# Ամենաերկար աճող ենթահաջորդականություն
# Տրված է n երկարությունունեցող թվերի X = [x1, x2, ... xn] հաջորդականությունը։
# X-ի S = [xi1, xi2, ... xin] (որտեղ 1 ≤ i1 < i2 < i3 < ... ≤ n  ենթահաջորդականությունը կոչվouմ է խիստ աճող,
# եթե xi1 < xi2 < ... < xin
# Պահանջվում է գտնել X հաջորդականության ամենաերկար խիստ աճող ենթահաջորդականությունը`
# L = max|S|, S ⊆ X, որտեղ S-ը աճող է։
# Օրինակ՝
# Մուտք X = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# Ելք LIS = [10, 22, 33, 50, 60, 80] (երկարությունը՝ 6)
# 1. Քննարկել խնդրի brute force լուծումը․
# 2. Սահմանել lis(i) ֆունկցիան։
# 3. Լուծել ռեկուրսիվ, գտնելով միայն ամենաերկար աճող ենթահաջորդականության երկարությունը։
# 4. Ներկայացնել կանչերի ծառը օրինակի համար։
# 5. Կիրառել DP տեխնիկան, կրկնակի կանչերից խուսափելու համար։ Իրականացնել top-down (memoizaon) և boom-up (tabulaon) մեթոդներով։
# 6. Ձևափոխել ֆունկցիան այնպես, որ արդյունքում ստանանք ամենաերկար խիստ աճող ենթահաջորդականությունը։

# Not a good approach , [0,1,0,3,2,3]
# def length_of_lis(nums):
#     lists = []
#     for i in range(0, len(nums)):
#         seq = 1
#         temp = nums[i]
#         for j in range(i + 1, len(nums)):
#             if temp < nums[j]:
#                 seq += 1
#                 temp = nums[j]
#         lists.append(seq)
#     count = max(lists)
#     return count

from datetime import datetime
from typing import List


def lis_recursive(nums: List[int], idx_n: int) -> int:
    if idx_n == 0:
        return 1

    max_lis: int = 1
    for prev in range(idx_n):
        if nums[prev] < nums[idx_n]:
            max_lis = max(max_lis, lis_recursive(nums, prev) + 1)
    return max_lis


def lis(nums: List[int]) -> int:
    n: int = len(nums)
    max_lis: int = 1
    for idx in range(1, n):
        max_lis = max(max_lis, lis_recursive(nums, idx))
    return max_lis


def lis_recursive_with_memoization(nums: List[int], idx_n: int, memo: List[int]) -> int:
    if memo[idx_n] != -1:
        return memo[idx_n]

    max_lis: int = 1

    for i in range(idx_n):
        if nums[i] < nums[idx_n]:
            max_lis = max(max_lis, lis_recursive_with_memoization(nums, i, memo) + 1)

    memo[idx_n] = max_lis
    return memo[idx_n]


def lis_with_memoization(nums: List[int]) -> int:
    len_nums: int = len(nums)
    memo: List[int] = [-1] * len_nums
    memo[0] = 1
    for i in range(1, len_nums):
        lis_recursive_with_memoization(nums, i, memo)

    return max(memo)


def lis_with_tabulation(nums: List[int]) -> int:
    len_nums: int = len(nums)
    dp: List[int] = [1] * len_nums

    for i in range(1, len_nums):
        for j in range(0, i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_elements(nums: List[int]) -> List[int]:
    len_nums: int = len(nums)
    dp: List[int] = [1] * len_nums
    prev_indexes: List[int] = [-1] * len_nums

    for i in range(1, len_nums):
        for j in range(0, i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = max(dp[i], dp[j] + 1)
                prev_indexes[i] = j

    max_index: int = dp.index(max(dp))
    lis_arr: List[int] = []
    while max_index != -1:
        lis_arr.append(nums[max_index])
        max_index = prev_indexes[max_index]
    lis_arr.reverse()

    return lis_arr


def test_lis(arr: List[int]):
    start_time: datetime = datetime.now()
    lis_len: int = lis(arr)
    print(f"Duration: {datetime.now() - start_time} (without optimization). Length of lis {arr} : {lis_len}")


def test_lis_with_memoization(arr: List[int]):
    start_time: datetime = datetime.now()
    lis_len: int = lis_with_memoization(arr)
    print(f"Duration: {datetime.now() - start_time} (with memoization    ). Length of lis {arr} : {lis_len}")


def test_lis_with_tabulation(arr: List[int]):
    start_time: datetime = datetime.now()
    lis_len: int = lis_with_tabulation(arr)
    print(f"Duration: {datetime.now() - start_time} (with tabulation     ). Length of lis {arr} : {lis_len}")


def test_lis_elements(arr: List[int]):
    start_time: datetime = datetime.now()
    lis_result: List[int] = lis_elements(arr)
    print(f"Duration: {datetime.now() - start_time} (with tabulation     ). Lis for {arr} : {lis_result}")


def test_lis_with_all_ways(arr: List[int]):
    test_lis(arr)
    test_lis_with_memoization(arr)
    test_lis_with_tabulation(arr)
    test_lis_elements(arr)


if __name__ == "__main__":
    test_lis_with_all_ways([0, 1, 0, 3, 2, 3])
    test_lis_with_all_ways([10, 22, 9, 33, 21, 50, 41, 60, 80])
    test_lis_with_all_ways([7, 7, 7, 7, 7, 7])
    test_lis_with_all_ways([10, 9, 2, 5, 3, 7, 101, 18])
    test_lis_with_all_ways([120, 340, 150, 200, 500, 20])
