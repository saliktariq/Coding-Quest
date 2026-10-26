"""
# Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

## Sample Input

```
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

## Sample Output

```
[-1, 11] // the numbers could be in reverse order
```
"""

""" def two_num_sum(array: list[int], target: int) -> list[int]:
    for a in array:
        if target - a in array and array.index(a) != array.index(target - a):
            return [a, target - a]
    return []
    //O(n^2) ince in array runs in O(n)
 """


def two_num_sum(array: list[int], target: int) -> list[int]:
    seen = set()
    for item in array:
        if target - item in seen:
            return [target - item, item]
        seen.add(item)
    return []


# time and space both O(n)

print(two_num_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
