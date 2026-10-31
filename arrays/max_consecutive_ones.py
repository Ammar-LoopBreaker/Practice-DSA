# Question: Find the maximum number of consecutive 1s in a binary array.
# Example: [1, 1, 0, 1, 1, 1] -> 3
"""Longest run of consecutive 1s in a binary array."""


def max_consecutive_ones(nums: list) -> int:
    """Track the current streak and the best streak seen."""
    best = cur = 0
    for x in nums:
        cur = cur + 1 if x == 1 else 0      # reset on any 0
        best = max(best, cur)
    return best


if __name__ == "__main__":
    print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))  # 3
