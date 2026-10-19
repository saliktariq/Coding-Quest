"""
# Nth Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..

## Sample Input #1

```
n = 2
```

## Sample Output #1

```
1 // 0, 1
```

## Sample Input #2

```
n = 6
```

## Sample Output #2

```
5 // 0, 1, 1, 2, 3, 5
```
"""

# O(n) time and O(n) space solution
# def nth_fibonacci_number(num: int) -> int:
#     return _fib_gen(num)[-1]


# def _fib_gen(num: int) -> list[int]:
#     if num < 1:
#         raise ValueError("Enter a positive number greater than or equal to 1")
#     if num == 1:
#         return [0]
#     if num == 2:
#         return [0, 1]
#     result: list[int] = [0, 1]
#     for _ in range(2, num):
#         result.append(result[-1] + result[-2])
#     return result

# print(nth_fibonacci_number(4))


# Time: O(n), Space: O(1), assumes O(1) integer addition
def nth_fibonacci_number(num: int) -> int:
    if num < 1:
        raise ValueError("Enter a positive number")
    second_last, last = 0, 1
    for _ in range(int(num) - 2):
        second_last, last = last, second_last + last
    return last


print(nth_fibonacci_number(6))
