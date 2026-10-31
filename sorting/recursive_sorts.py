# Question: Implement Bubble Sort and Insertion Sort using recursion.
# Example: [5, 3, 1, 4] -> [1, 3, 4, 5]
"""Recursive versions of Bubble Sort and Insertion Sort."""
from typing import Optional


def recursive_bubble_sort(arr: list, n: Optional[int] = None) -> list:
    """Each call bubbles the max of arr[:n] to index n-1, then recurses on n-1."""
    n = len(arr) if n is None else n
    if n <= 1:
        return arr
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return recursive_bubble_sort(arr, n - 1)


def recursive_insertion_sort(arr: list, n: Optional[int] = None) -> list:
    """Sort arr[:n-1] recursively, then insert arr[n-1] into it."""
    n = len(arr) if n is None else n
    if n <= 1:
        return arr
    recursive_insertion_sort(arr, n - 1)
    key, j = arr[n - 1], n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    return arr


if __name__ == "__main__":
    print(recursive_bubble_sort([5, 3, 1, 4]))     # [1, 3, 4, 5]
    print(recursive_insertion_sort([5, 3, 1, 4]))  # [1, 3, 4, 5]
