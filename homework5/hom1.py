# 1. Տրված str1 և str2 տողերի համար հաշվել դրանք հավասար դարձնելու համար պահանջվող նվազագյն քայլերը։
# Յուրաքանչյուր քայլին կարելի է ջնջել ընդհամենը մեկ տառ։ Վերադարձնել ջնջված տառերի զանգվածը, որում սկզբում կլինեն str1,
# այնուհետև str2 տողի տառերը ըստ հերթականթյան։
# Օրինակ։
# Input: str1 = "sea", str2 = "eat"
# Output: [s, t], (str1 տողից հեռացվում է ‘s’-ը, str2-ից՝ ‘t’-ն)։
from typing import List


def equalize_the_sequences_with_tabulation(str1, str2, n, m):
    dp: List[List[int]] = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    removing_for_str1 = []
    removing_for_str2 = []

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                # dp[i][j] = dp[i - 1][j - 1] + 1
                continue
            else:
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                pass
    return dp[n][m]


if __name__ == "__main__":
    pass
