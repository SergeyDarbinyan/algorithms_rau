# 1. (60 միավոր) Արարատն ունի գրադարան, որտեղ պահում է N հատ գիրք։ Գրքերը դասավորված են որոշակի հերթականությամբ և
# համարակալված են 0-ից N−1։ Արարատը ցանկանում է կարդալ իր գրքերն ըստ հերթականության այնպես, որ յուրաքանչյուր հաջորդ
# ընտրված գիրքը ունենա ավելի շատ էջեր, քան նախորդը։
# Օգնեք Արարատին որոշել գրքերի ճիշտ հաջորդականությունն այնպես, որ ընթերցված գրքերի քանակը լինի առավելագույնը։
# Օրինակ՝ Մուտք` pages =[120, 340, 150, 200, 500, 20]
# Ելք` [0, 2, 3, 4]

from datetime import datetime
from typing import List


def lis_indexes(nums: List[int]) -> List[int]:
    len_nums: int = len(nums)
    dp: List[int] = [1] * len_nums
    prev_indexes: List[int] = [-1] * len_nums

    for i in range(1, len_nums):
        for j in range(0, i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = max(dp[i], dp[j] + 1)
                prev_indexes[i] = j

    max_index: int = dp.index(max(dp))
    lis_indexes_arr: List[int] = []
    while max_index != -1:
        lis_indexes_arr.append(max_index)
        max_index = prev_indexes[max_index]
    lis_indexes_arr.reverse()

    return lis_indexes_arr


def my_test_lis_indexes(arr: List[int]):
    start_time: datetime = datetime.now()
    lis_indexes_result: List[int] = lis_indexes(arr)
    print(f"Duration: {datetime.now() - start_time} (with tabulation     ). Lis for pages {arr} : {lis_indexes_result}")


if __name__ == "__main__":
    my_test_lis_indexes([120, 340, 150, 200, 500, 20])
    my_test_lis_indexes([50, 60, 70, 80, 90, 100])
    my_test_lis_indexes([100, 90, 80, 70, 60, 50])
    my_test_lis_indexes([150, 200, 80, 120, 180, 300])
    my_test_lis_indexes([150, 150, 150, 150, 150, 150])
