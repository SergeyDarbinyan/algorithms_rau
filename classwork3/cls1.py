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
def count_rod_max_price(rod_len: int, prices: dict[int:int]) -> int:
    if rod_len == 0:
        return 0
    max_num: int = prices[rod_len]
    for i in range(1, rod_len):
        max_num = max(max_num, prices[i] + count_rod_max_price(rod_len - i, prices))
    return max_num


def count_rod_max_price_with_memoization(rod_len: int, prices: dict[int:int], memo: List[int]) -> int:
    if rod_len == 0:
        return 0

    # 0-based indexing, for 1-based indexing can just use memo[num] in all places instead memo[mun-1]
    if memo[rod_len - 1] != -1:
        return memo[rod_len - 1]

    max_num: int = prices[rod_len]
    for i in range(1, rod_len):
        max_num = max(max_num, prices[i] + count_rod_max_price_with_memoization(rod_len - i, prices, memo))
    memo[rod_len - 1] = max_num
    return max_num


def count_rod_max_price_with_tabulation(rod_len: int, prices: dict[int:int]) -> int:
    if rod_len == 0:
        return 0

    dp: List[int] = [0] * (rod_len + 1)

    for i in range(1, rod_len + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j] + dp[i - j])

    return dp[rod_len]


def count_rod_max_price_and_breakdowns_with_tabulation(rod_len: int, prices: dict[int:int]) -> tuple[int: List[int]]:
    if rod_len == 0:
        return 0

    dp: List[int] = [0] * (rod_len + 1)
    cut_indexes: List[int] = [0] * (rod_len + 1)

    for i in range(1, rod_len + 1):
        for j in range(1, i + 1):
            if dp[i] < prices[j] + dp[i - j]:
                dp[i] = prices[j] + dp[i - j]
                cut_indexes[i] = j

    len_indexes_of_max_price: List[int] = []
    remaining_rod_len: int = rod_len
    while remaining_rod_len > 0:
        len_indexes_of_max_price.append(cut_indexes[remaining_rod_len])
        remaining_rod_len -= cut_indexes[remaining_rod_len]
    return dp[rod_len], len_indexes_of_max_price


def test_rod_max_price(rod_len: int, prices: dict[int:int]):
    start_time: datetime = datetime.now()
    rod_max_price: int = count_rod_max_price(rod_len, prices)
    print(f"Duration: {datetime.now() - start_time} (without optimization). Price for {rod_len} : {rod_max_price}")


def test_rod_max_price_with_memoization(rod_len: int, prices: dict[int:int]):
    start_time: datetime = datetime.now()
    memo: List[int] = [-1] * len(metr_price_pairs)
    rod_max_price: int = count_rod_max_price_with_memoization(rod_len, prices, memo)
    print(f"Duration: {datetime.now() - start_time} (with memoization    ). Price for {rod_len} : {rod_max_price}")


def test_rod_max_price_with_tabulation(rod_len: int, prices: dict[int:int]):
    start_time: datetime = datetime.now()
    rod_max_price: int = count_rod_max_price_with_tabulation(rod_len, prices)
    print(f"Duration: {datetime.now() - start_time} (with tabulation     ). Price for {rod_len} : {rod_max_price}")


def test_rod_max_price_and_breakdowns_with_tabulation(rod_len: int, prices: dict[int:int]):
    start_time: datetime = datetime.now()
    rod_max_price_and_breakdowns: tuple[int:List[int]] = count_rod_max_price_and_breakdowns_with_tabulation(rod_len,
                                                                                                            prices)
    print(
        f"Duration: {datetime.now() - start_time} (with tabulation     ). Price for {rod_len} : {rod_max_price_and_breakdowns[0]}. Breakdowns : {rod_max_price_and_breakdowns[1]}.")


def test_rod_max_price_all_ways(num: int, prices: dict[int:int]):
    test_rod_max_price(num, prices)
    test_rod_max_price_with_memoization(num, prices)
    test_rod_max_price_with_tabulation(num, prices)
    test_rod_max_price_and_breakdowns_with_tabulation(num, prices)


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
