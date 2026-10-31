# Question: Given n distinct numbers from 0 to n, find the one missing number.
# Example: [3, 0, 1] -> 2
"""Missing number from 0..n in an array of n distinct numbers."""


def missing_number(nums: list) -> int:
    """Expected sum of 0..n minus actual sum: O(n) time, O(1) space."""
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))  # 2
