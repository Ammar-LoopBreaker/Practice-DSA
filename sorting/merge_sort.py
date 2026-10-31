# Question: Sort an array using divide and conquer: split in halves, sort each, merge (Merge Sort).
# Example: [38, 27, 43, 3, 9, 82, 10] -> [3, 9, 10, 27, 38, 43, 82]
"""Merge Sort: O(n log n) time, O(n) space, stable."""


def merge_sort(arr: list) -> list:
    """Return a new sorted list using divide and conquer."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):     # merge two sorted halves
        if left[i] <= right[j]:                 # <= keeps the sort stable
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]        # append the leftovers


if __name__ == "__main__":
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
