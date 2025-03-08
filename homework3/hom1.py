# 1. Ամբողջաթիվ f(n) ֆունկցիան n ≥ 0 համար սահմանվում է հետևյալ ռեկուրսիվ եղանակով․
# f(n) = f(n − 1) + 2f(n − 2) − 3f(n − 3) + 1, n ≥ 3
# f(2) = 2, f(1) = 1, f(0) = 0
# ➢ Անմիջականորեն հաշվել f(10) արժեքը:
# ➢ Կառուցել f(n) արժեքը հաշվարկող ռեկուրսիվ ֆունկցիա և օգտագործել այն f(10) արժեքը հաշվելու համար։
# ➢ Կառուցել f(n) արժեքը դինամիկ ծրագրավորման top-down (memoizaon) մեթոդով հաշվարկող ֆունկցիա և օգտագործել այն f(10) արժեքը հաշվելու համար։
# ➢ Կառուցել f(n) արժեքը դինամիկ ծրագրավորման buom-up (tabulaon) մեթոդով հաշվարկող ֆունկցիա և օգտագործել այն f(10) արժեքը հաշվելու համար։
# ➢ Վերը նշված երեք տարբերակներով (այն է, ռեկուրսիվ, DP top-down, DP boom-up) հաշվել f(500) արժեքը։ Յրաքանչյուր դեպքում տպել ծախսած ժամանակը՝ միկրովարկյաններով։
# ➢ Կառցել ֆունկցիա, որը մուտքում ստանալով k երկարթյուն ունեցող indexes զանգվածը, կհաշվի և կվերադարձնի [f(index[0]), f(index[1],․․․, f(index[k]] զանգվածը։

from datetime import datetime
from typing import List


def fibonacci_like_function(num: int) -> int:
    if num in (0, 1, 2):
        return num

    return fibonacci_like_function(num - 1) + 2 * fibonacci_like_function(num - 2) - 3 * fibonacci_like_function(
        num - 3) + 1


def fibonacci_like_function_with_memorization(num: int, memo: dict[int:int]) -> int:
    if num in memo:
        return memo[num]

    memo[num] = fibonacci_like_function_with_memorization(num - 1,
                                                          memo) + 2 * fibonacci_like_function_with_memorization(
        num - 2, memo) - 3 * fibonacci_like_function_with_memorization(
        num - 3, memo) + 1

    return memo[num]


def fibonacci_like_function_with_tabulation(num: int) -> int:
    dp: List[int] = [0] * (num + 1)
    dp[0], dp[1], dp[2] = 0, 1, 2

    for i in range(3, num + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2] - 3 * dp[i - 3] + 1

    return dp[num]


def fibonacci_like_function_elements(num: int) -> List[int]:
    dp: List[int] = [0] * (num + 1)
    dp[0], dp[1], dp[2] = 0, 1, 2

    for i in range(3, num + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2] - 3 * dp[i - 3] + 1

    return dp


def test_fibonacci_like_function(num: int):
    start_time: datetime = datetime.now()
    result: int = fibonacci_like_function(num)
    print(f"Duration: {datetime.now() - start_time} (without optimization). Result for {num} : {result}")


def test_fibonacci_like_function_with_memoization(num: int):
    start_time: datetime = datetime.now()
    memo: dict[int:int] = {0: 0, 1: 1, 2: 2}
    result: int = fibonacci_like_function_with_memorization(num, memo)
    print(f"Duration: {datetime.now() - start_time} (with memoization    ). Result for {num} : {result}")


def test_fibonacci_like_function_with_tabulation(num: int):
    start_time: datetime = datetime.now()
    result: int = fibonacci_like_function_with_tabulation(num)
    print(f"Duration: {datetime.now() - start_time} (with tabulation     ). Result for {num} : {result}")


def test_fibonacci_like_function_elements(num: int):
    start_time: datetime = datetime.now()
    result: List[int] = fibonacci_like_function_elements(num)
    print(f"Duration: {datetime.now() - start_time}. Elements for {num} : {result}")


def test_fibonacci_like_function_with_all(num: int):
    if num < 32:
        test_fibonacci_like_function(num)
    else:
        print(f"Duration: is too long to initialize for {num}. Skipping...")
    test_fibonacci_like_function_with_memoization(num)
    test_fibonacci_like_function_with_tabulation(num)
    test_fibonacci_like_function_elements(num)


if __name__ == "__main__":
    test_fibonacci_like_function_with_all(10)
    test_fibonacci_like_function_with_all(25)
    test_fibonacci_like_function_with_all(31)
    test_fibonacci_like_function_with_all(500)
