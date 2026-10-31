# Question: Rotate an array to the left by k places.
# Example: [1, 2, 3, 4, 5, 6, 7], k=3 -> [4, 5, 6, 7, 1, 2, 3]
"""Left-rotate an array by k places using the reversal algorithm: O(n), O(1) space."""


def left_rotate(arr: list, k: int) -> list:
    """Rotate `arr` left by k positions in place."""
    n = len(arr)
    if n == 0:
        return arr
    k %= n

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo, hi = lo + 1, hi - 1

    reverse(0, k - 1)      # reverse first k
    reverse(k, n - 1)      # reverse the rest
    reverse(0, n - 1)      # reverse everything
    return arr


if __name__ == "__main__":
    print(left_rotate([1, 2, 3, 4, 5, 6, 7], 3))  # [4, 5, 6, 7, 1, 2, 3]
