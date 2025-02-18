def count_max_sum(num: int, prices: dict[int:int]) -> int:
    if num == 0:
        return 0
    max_num: int = prices[num]
    for i in range(1, num):
        max_num = max(max_num, prices[i] + count_max_sum(num - i, prices))
    return max_num


if __name__ == "__main__":
    metr_price_pairs: dict[int:int] = {
        0: 0,
        1: 1,
        2: 5,
        3: 6,
        4: 9,
        5: 10,
        6: 13,
        7: 17,
        8: 19,
        9: 21,
        10: 22,
        11: 25,
        12: 27,
        13: 28
    }
    print(count_max_sum(13, metr_price_pairs))
