# Question: Every element appears twice except one. Find the element that appears once.
# Example: [4, 1, 2, 1, 2] -> 4
"""Find the element that appears once when all others appear twice (XOR trick)."""
from functools import reduce
from operator import xor


def single_number(nums: list) -> int:
    """a ^ a = 0 and a ^ 0 = a, so pairs cancel out. O(n) time, O(1) space."""
    return reduce(xor, nums, 0)


if __name__ == "__main__":
    print(single_number([4, 1, 2, 1, 2]))  # 4
