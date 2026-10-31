# Question: Move all zeros to the end of the array while keeping the order of the other elements.
# Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
"""Move all zeros to the end while keeping the order of non-zeros."""


def move_zeros(arr: list) -> list:
    """Two-pointer in-place solution: O(n) time, O(1) space."""
    j = 0                                   # next slot for a non-zero
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
