# Question: Check whether an array is sorted in non-decreasing order.
# Example: [1, 2, 2, 5] -> True, [1, 3, 2] -> False
"""Check whether an array is sorted in non-decreasing order."""


def is_sorted(arr: list) -> bool:
    """Return True if every element is <= its successor."""
    return all(a <= b for a, b in zip(arr, arr[1:]))


if __name__ == "__main__":
    print(is_sorted([1, 2, 2, 5]))  # True
    print(is_sorted([1, 3, 2]))     # False
