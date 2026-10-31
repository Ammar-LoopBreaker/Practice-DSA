# Question: Find the first and last position of a value in a sorted array.
# Example: [1,2,2,2,5], x=2 -> (1, 3)
"""First and last occurrence of a value (and its count) in a sorted array."""


def _bound(arr: list, x, strict: bool) -> int:
    """strict=False -> lower bound; strict=True -> upper bound."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x or (strict and arr[mid] == x):
            lo = mid + 1
        else:
            hi = mid
    return lo


def first_last(arr: list, x) -> tuple:
    """Return (first_index, last_index) of x, or (-1, -1) if absent."""
    first = _bound(arr, x, False)
    if first == len(arr) or arr[first] != x:
        return -1, -1
    return first, _bound(arr, x, True) - 1


if __name__ == "__main__":
    a = [1, 2, 2, 2, 5]
    f, l = first_last(a, 2)
    print(f, l, "count =", l - f + 1)  # 1 3 count = 3
