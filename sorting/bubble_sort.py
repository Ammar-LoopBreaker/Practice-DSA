# Question: Sort an array by repeatedly swapping adjacent elements that are out of order (Bubble Sort).
# Example: [5, 1, 4, 2, 8] -> [1, 2, 4, 5, 8]
"""Bubble Sort: O(n^2) worst, O(n) best (already sorted), stable."""


def bubble_sort(arr: list) -> list:
    """Sort `arr` in place by bubbling the largest value to the end each pass."""
    n = len(arr)
    for end in range(n - 1, 0, -1):
        swapped = False
        for j in range(end):
            if arr[j] > arr[j + 1]:        # adjacent pair out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:                    # no swaps -> already sorted
            break
    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
