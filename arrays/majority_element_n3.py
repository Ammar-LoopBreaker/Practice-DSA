# Question: Find all elements that appear more than n/3 times in the array.
# Example: [1, 1, 1, 3, 3, 2, 2, 2] -> [1, 2]
"""Majority Element II: all elements appearing more than n/3 times."""


def majority_element_n3(nums: list) -> list:
    """Extended Boyer-Moore with two candidates, then verify. O(n), O(1) space."""
    e1 = e2 = None
    c1 = c2 = 0
    for x in nums:
        if x == e1:
            c1 += 1
        elif x == e2:
            c2 += 1
        elif c1 == 0:
            e1, c1 = x, 1
        elif c2 == 0:
            e2, c2 = x, 1
        else:                               # x differs from both: cancel one vote each
            c1, c2 = c1 - 1, c2 - 1
    return [e for e in (e1, e2) if e is not None and nums.count(e) > len(nums) // 3]


if __name__ == "__main__":
    print(majority_element_n3([1, 1, 1, 3, 3, 2, 2, 2]))  # [1, 2]
