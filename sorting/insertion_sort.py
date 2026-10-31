# Question: Sort an array by inserting each element into its correct place in the sorted part (Insertion Sort).
# Example: [12, 11, 13, 5, 6] -> [5, 6, 11, 12, 13]
"""Insertion Sort: O(n^2) worst, O(n) best, stable, great for small/nearly sorted data."""


def insertion_sort(arr: list) -> list:
    """Sort `arr` in place by inserting each element into the sorted prefix."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:     # shift larger elements right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key                   # drop key into its slot
    return arr


if __name__ == "__main__":
    print(insertion_sort([12, 11, 13, 5, 6]))  # [5, 6, 11, 12, 13]
