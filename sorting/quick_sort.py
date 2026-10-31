# Question: Sort an array by partitioning around a pivot and sorting each side (Quick Sort).
# Example: [10, 7, 8, 9, 1, 5] -> [1, 5, 7, 8, 9, 10]
"""Quick Sort: O(n log n) average, O(n^2) worst, in place, not stable."""
from typing import Optional


def quick_sort(arr: list, low: int = 0, high: Optional[int] = None) -> list:
    """Sort `arr` in place using Lomuto partitioning around the last element."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot, i = arr[high], low
        for j in range(low, high):             # move smaller-than-pivot items left
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]  # pivot lands in its final spot
        quick_sort(arr, low, i - 1)
        quick_sort(arr, i + 1, high)
    return arr


if __name__ == "__main__":
    print(quick_sort([10, 7, 8, 9, 1, 5]))  # [1, 5, 7, 8, 9, 10]
