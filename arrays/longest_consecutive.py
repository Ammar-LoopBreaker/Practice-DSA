# Question: Find the length of the longest run of consecutive integers in an unsorted array.
# Example: [100, 4, 200, 1, 3, 2] -> 4
"""Longest consecutive sequence in an unsorted array: O(n) with a set."""


def longest_consecutive(nums: list) -> int:
    """Only start counting from numbers that begin a sequence."""
    values, best = set(nums), 0
    for x in values:
        if x - 1 not in values:             # x is a sequence start
            length = 1
            while x + length in values:
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4
