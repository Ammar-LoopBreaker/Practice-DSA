# Question: Sort an array by repeatedly selecting the smallest remaining element (Selection Sort).
# Example: [64, 25, 12, 22, 11] -> [11, 12, 22, 25, 64]
"""Selection Sort: O(n^2) time, O(1) space, not stable."""


def selection_sort(arr: list) -> list:
    """Sort `arr` in place by repeatedly selecting the minimum of the unsorted part."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):          # find smallest element in arr[i:]
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # place it at position i
    return arr


if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]
