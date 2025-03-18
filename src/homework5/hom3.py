# 3. Տրված str տողում գտնել ամենաերկար պալինդրոմ հաջորդականությունը։ Հաշվել ալգորիթմի ժամանակային բարդությունը։
# Օրինակ։ Input: str = "character", Output: “carac”

from datetime import datetime
from typing import List


# def lps_with_memoization(s, low, high, memo=None):
#     if not memo:
#         memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
#     if low > high:
#         return 0
#     if low == high:
#         return 1
#     if memo[low][high] != -1:
#         return memo[low][high]
#
#     if s[low] == s[high]:
#         memo[low][high] = lps_with_memoization(s, low + 1, high - 1, memo) + 2
#     else:
#         memo[low][high] = max(lps_with_memoization(s, low + 1, high, memo),
#                               lps_with_memoization(s, low, high - 1, memo))
#     return memo[low][high]

def lps_substr_with_tabulation(str1: str) -> str:
    if not str1:
        return ""
    n: int = len(str1)
    dp: List[List[int]] = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
                continue
            if str1[i] == str1[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    i: int = 0
    j: int = n - 1
    lps: List[str] = []
    while i <= j:
        if str1[i] == str1[j]:
            lps.append(str1[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    second_part: List[str] = lps[:] if len(lps) * 2 == dp[0][n - 1] else lps[:-1]
    return ''.join(lps + second_part[::-1])


def my_test_lps_substr_with_tabulation(str1: str):
    start_time: datetime = datetime.now()
    lps: str = lps_substr_with_tabulation(str1)
    print(
        f"Duration: {datetime.now() - start_time} (with tabulation     ). Lps of {str1} : {lps}")


def my_test_lps_cases():
    my_test_lps_substr_with_tabulation('abcde')
    my_test_lps_substr_with_tabulation('abba')
    my_test_lps_substr_with_tabulation('racecar')
    my_test_lps_substr_with_tabulation('z')
    my_test_lps_substr_with_tabulation('aaaaa')
    my_test_lps_substr_with_tabulation('agbdba')
    my_test_lps_substr_with_tabulation('abcbad')
    my_test_lps_substr_with_tabulation('abacdfgdcaba')
    my_test_lps_substr_with_tabulation('')
    my_test_lps_substr_with_tabulation('diuacsjh')


if __name__ == "__main__":
    my_test_lps_cases()
