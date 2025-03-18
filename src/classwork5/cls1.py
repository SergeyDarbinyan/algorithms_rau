# Ամենաերկար ընդհանուր ենթահաջորդականությունը
# 1143. Longest Common Subsequence - LeetCode
# Տրված է n երկարություն ունեցող str1 և m երկարություն ունեցող srt2 հաջորդականությունները։
# Պահանջվում է գտնել str1 և str2 հաջորդականությունների ամենաերկար ընդհանուր ենթահաջորդականությունը։
# Օրինակ՝
# Մուտք str1 = "abcde", str2 = "ace"
# Ելք LCS = “ace” (երկարությունը՝ 3)
# 1. Քննարկել խնդրի brute force լուծումը:
# 2. Սահմանել lcs(i, j) ֆունկցիան։
# 3. Լուծել ռեկուրսիվ, գտնելով միայն ամենաերկար ընդհանուր ենթահաջորդականության երկարությունը։
# 4. Ներկայացնել կանչերի ծառը օրինակի համար։
# 5. Կիրառել DP տեխնիկան, կրկնակի կանչերից խուսափել համար։ Իրականացնել top-down (memoizaon) և boom-up (tabulaon) մեթոդներով։
# 6. Ձևափոխել ֆունկցիան այնպես, որ արդյունքում ստանանք ամենաերկար պալինդրոմ ենթահաջորդականությունը։
# 7. Իրականացնել lcs(str1, str2, str3) ֆունկցիան։
from datetime import datetime
from typing import List


def lcs_recursive(str1: str, str2: str, n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0

    if str1[n - 1] == str2[m - 1]:
        return 1 + lcs_recursive(str1, str2, n - 1, m - 1)

    return max(lcs_recursive(str1, str2, n - 1, m), lcs_recursive(str1, str2, n, m - 1))


def lcs_with_memoization(str1: str, str2: str, n: int, m: int, memo: List[List[int]] = None) -> int:
    if not memo:
        memo = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    if n == 0 or m == 0:
        return 0
    if memo[n][m] != -1:
        return memo[n][m]

    if str1[n - 1] == str2[m - 1]:
        memo[n][m] = 1 + lcs_with_memoization(str1, str2, n - 1, m - 1, memo)
        return memo[n][m]

    memo[n][m] = max(lcs_with_memoization(str1, str2, n - 1, m, memo), lcs_with_memoization(str1, str2, n, m - 1, memo))
    return memo[n][m]


def lcs_with_tabulation(str1: str, str2: str, n: int, m: int) -> int:
    dp: List[List[int]] = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def lcs_string_with_tabulation(str1: str, str2: str, n: int, m: int) -> str:
    dp: List[List[int]] = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_str = []
    i, j = n, m
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = ''.join(reversed(lcs_str))
    return lcs


def my_test_lcs(str1: str, str2: str, n: int, m: int):
    start_time: datetime = datetime.now()
    lcs_len: int = lcs_recursive(str1, str2, n, m)
    print(
        f"Duration: {datetime.now() - start_time} (without optimization). Length of lcs {str1} and {str2} : {lcs_len}")


def my_test_lcs_with_memoization(str1: str, str2: str, n: int, m: int):
    start_time: datetime = datetime.now()
    lcs_len: int = lcs_with_memoization(str1, str2, n, m)
    print(
        f"Duration: {datetime.now() - start_time} (with memoization    ). Length of lcs {str1} and {str2} : {lcs_len}")


def my_test_lcs_with_tabulation(str1: str, str2: str, n: int, m: int):
    start_time: datetime = datetime.now()
    lcs_len: int = lcs_with_tabulation(str1, str2, n, m)
    print(
        f"Duration: {datetime.now() - start_time} (with tabulation     ). Length of lcs {str1} and {str2} : {lcs_len}")


def my_test_lcs_string_with_tabulation(str1: str, str2: str, n: int, m: int):
    start_time: datetime = datetime.now()
    lcs: str = lcs_string_with_tabulation(str1, str2, n, m)
    print(
        f"Duration: {datetime.now() - start_time} (with tabulation     ). LCS of {str1} and {str2} : {lcs}")


def my_test_lcs_with_all_ways(str1: str, str2: str):
    my_test_lcs(str1, str2, len(str1), len(str2))
    my_test_lcs_with_memoization(str1, str2, len(str1), len(str2))
    my_test_lcs_with_tabulation(str1, str2, len(str1), len(str2))
    my_test_lcs_string_with_tabulation(str1, str2, len(str1), len(str2))


def my_test_lcs_cases():
    my_test_lcs_with_all_ways('abcde', 'ace')
    my_test_lcs_with_all_ways("abc", "xyz")
    my_test_lcs_with_all_ways("abcdef", "abcdef")
    my_test_lcs_with_all_ways("abc", "aabbcc")
    my_test_lcs_with_all_ways("aaaabbbb", "ababab")
    my_test_lcs_with_all_ways("aarfbyhkjkmnvvgfrdgujlolpmnhk", "eqsrfygi")
    my_test_lcs_with_all_ways("AGGTAB", "GXTXAYB")
    my_test_lcs_with_all_ways("abc", "")
    my_test_lcs_with_all_ways("", "")


if __name__ == "__main__":
    my_test_lcs_cases()
