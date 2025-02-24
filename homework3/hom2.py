# 2. Դիցուք ունեք N կիլոգրամ կշռով շաքարավազի պարկ, և prices զանգվածը, այնպես, որ prices[i] ցույց է տալիս i կիլոգրամ շաքարավազի
# գինը prices.size() >= N: Պարկում եղած շաքարավազն այնպես բաժանեք փոքր պարկերի մեջ, որ ստանաք առավելագույն եկամուտ։
# Վերադարձրեք բաժանված պարկերի քաշերը (կամայական հերթականությամբ)։
# Օրինակ՝ Մտք` n=4, prices = [1, 5, 8, 9]
# Ելք` [2,2]

from datetime import datetime
from typing import List


def count_sugar_box_max_price(box_kg: int, prices: List[int]) -> List[int]:
    if box_kg == 0:
        return []
    dp = [0] * (box_kg + 1)
    cut_indexes = [0] * (box_kg + 1)

    for i in range(1, box_kg + 1):
        for j in range(1, i + 1):
            if dp[i] < prices[j] + dp[i - j]:
                dp[i] = prices[j] + dp[i - j]
                cut_indexes[i] = j

    kg_indexes_of_max_price = []
    remaining_kg = box_kg
    while remaining_kg > 0:
        kg_indexes_of_max_price.append(cut_indexes[remaining_kg])
        remaining_kg -= cut_indexes[remaining_kg]
    return kg_indexes_of_max_price


def test_sugar_box_max_price(box_kg, prices):
    start_time: datetime = datetime.now()
    result: List[int] = count_sugar_box_max_price(box_kg, prices)
    print(f"Duration: {datetime.now() - start_time}. Indexes for {box_kg} : {result}")


if __name__ == "__main__":
    test_sugar_box_max_price(4, [0, 1, 5, 8, 9])
    test_sugar_box_max_price(5, [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    test_sugar_box_max_price(8, [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
