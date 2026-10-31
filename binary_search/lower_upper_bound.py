# Question: Find the lower bound, upper bound and insert position of x in a sorted array.
# Example: [1,2,2,2,5], x=2 -> lower 1, upper 4
"""Lower bound, upper bound and search-insert position."""


def lower_bound(arr: list, x) -> int:
    """First index i with arr[i] >= x (len(arr) if none)."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr: list, x) -> int:
    """First index i with arr[i] > x (len(arr) if none)."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    a = [1, 2, 2, 2, 5]
    print(lower_bound(a, 2), upper_bound(a, 2))  # 1 4
    print(lower_bound(a, 3))                     # 4  (search-insert position)
