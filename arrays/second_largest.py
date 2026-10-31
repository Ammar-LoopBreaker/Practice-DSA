# Question: Find the second largest distinct element in an array.
# Example: [12, 35, 1, 10, 34, 1] -> 34
"""Second largest distinct element in a single pass."""


def second_largest(arr: list):
    """Return the second largest distinct value, or None if it doesn't exist."""
    first = second = float("-inf")
    for x in arr:
        if x > first:
            first, second = x, first       # old max becomes runner-up
        elif first > x > second:           # strictly between -> new runner-up
            second = x
    return None if second == float("-inf") else second


if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 1]))  # 34
