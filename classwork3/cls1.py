# 1. Ձևակերպել ձողի տրոհման խնդիրը՝
# Տրված են n երկարություն ունեցող մետաղյա ձող և i = 1, 2, ..., n երկարութույնների արժողությունները։
# length i   1 2 3 4 5  6  7  8  9  10
# price p[i] 1 5 8 9 10 17 17 20 24 30
#
# Պահանջվում է գտնել ձողի այնպիսի (j1, j2, ..., jk) տրոհում (j1+ j2 + ․.. + jk = n), որն ապահովի առավելագույն արժեք՝
# r/n = p/j1 + p/j2 +... + p/jk
# գումարի համար:
# 2. Դուրս գրել բոլոր հնարավոր դեպքերը n=4 ի համար և հաշվել արժողություննը յուրաքանչյր դեպքի համար։
# 3. Ցույց տալ, որ չունի ագահ լուծում:
# 4. Լուծել ռեկուրսիվ։
# 5. Բերել օրինակ n=5 դեպքի համար, նշելով կառուցվող r զանգվածը։
# 6. Ցույց տալ ռեկուրսիվ կանչերի քանակը։
# 7. Կիրառել DP տեխնիկան, կրկնակի կանչերից խուսափել համար։ Իրականացնել top-down (memoizaon) և boom-up (tabulaon) մեթոդներով։
# 8. Ձևափոխել ֆունկցիան այնպես, որ արդյունքում ստանանք նաև օպտիմալ տրոհումները։
from datetime import datetime
from typing import List


# Simple solution without optimization
def count_max_sum(num: int, prices: dict[int:int]) -> int:
    if num == 0:
        return 0
    max_num: int = prices[num]
    for i in range(1, num):
        max_num = max(max_num, prices[i] + count_max_sum(num - i, prices))
    return max_num


def count_max_sum_with_memoization(num: int, prices: dict[int:int], memo: List[int]) -> int:
    if num == 0:
        return 0

    # 0-based indexing, for 1-based indexing can just use memo[num] in all places instead memo[mun-1]
    if memo[num - 1] != -1:
        return memo[num - 1]

    max_num: int = prices[num]
    for i in range(1, num):
        max_num = max(max_num, prices[i] + count_max_sum_with_memoization(num - i, prices, memo))
    memo[num - 1] = max_num
    return max_num


def count_max_sum_with_tabulation(num: int, prices: dict[int:int]) -> int:
    if num == 0:
        return 0

    dp = [0] * (num + 1)

    for i in range(1, num + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j] + dp[i - j])

    return dp[num]


def test_rod_max_price(num, prices):
    start_time = datetime.now()
    rod_max_price = count_max_sum(num, prices)
    print(f"Duration: {datetime.now() - start_time}. Price for {num} : {rod_max_price}")


def test_rod_max_price_with_memoization(num, prices):
    start_time = datetime.now()
    memo = [-1] * len(metr_price_pairs)
    rod_max_price = count_max_sum_with_memoization(num, prices, memo)
    print(f"Duration: {datetime.now() - start_time}. Price for {num} : {rod_max_price}")


def test_rod_max_price_with_tabulation(num, prices):
    start_time = datetime.now()
    rod_max_price = count_max_sum_with_tabulation(num, prices)
    print(f"Duration: {datetime.now() - start_time}. Price for {num} : {rod_max_price}")


def test_rod_max_price_all_ways(num, prices):
    test_rod_max_price(num, prices)
    test_rod_max_price_with_memoization(num, prices)
    test_rod_max_price_with_tabulation(num, prices)


if __name__ == "__main__":
    metr_price_pairs: dict[int:int] = {
        0: 0,
        1: 1,
        2: 5,
        3: 8,
        4: 9,
        5: 10,
        6: 17,
        7: 17,
        8: 20,
        9: 24,
        10: 30
    }
    test_rod_max_price_all_ways(5, metr_price_pairs)
    test_rod_max_price_all_ways(8, metr_price_pairs)
    test_rod_max_price_all_ways(10, metr_price_pairs)
