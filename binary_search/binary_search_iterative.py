# Question: Search for a target in a sorted array using iterative binary search.
# Example: [1,3,5,7,9,11], target=7 -> 3
"""Iterative Binary Search: O(log n) time, O(1) space. Array must be sorted."""


def binary_search(arr: list, target) -> int:
    """Return the index of target, or -1 if absent."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2           # avoids overflow in other languages
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1                    # discard left half
        else:
            hi = mid - 1                    # discard right half
    return -1


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9, 11], 7))  # 3
