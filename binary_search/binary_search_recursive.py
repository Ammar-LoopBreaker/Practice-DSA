# Question: Search for a target in a sorted array using recursive binary search.
# Example: [1,3,5,7,9,11], target=4 -> -1
"""Recursive Binary Search: O(log n) time, O(log n) call-stack space."""
from typing import Optional


def binary_search(arr: list, target, lo: int = 0, hi: Optional[int] = None) -> int:
    """Return the index of target in sorted `arr`, or -1."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:                             # base case: search space empty
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    return binary_search(arr, target, lo, mid - 1)


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9, 11], 4))  # -1
    print(binary_search([1, 3, 5, 7, 9, 11], 9))  # 4
