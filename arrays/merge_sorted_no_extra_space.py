# Question: Merge two sorted arrays without using extra space.
# Example: [1,4,8,10] and [2,3,9] -> [1,2,3,4] and [8,9,10]
"""Merge two sorted arrays without extra space (in place)."""


def merge_sorted(a: list, b: list) -> None:
    """Swap a's large tail with b's small head, then sort both. O((n+m) log(n+m))."""
    i, j = len(a) - 1, 0
    while i >= 0 and j < len(b) and a[i] > b[j]:
        a[i], b[j] = b[j], a[i]             # biggest of a <-> smallest of b
        i, j = i - 1, j + 1
    a.sort()
    b.sort()


if __name__ == "__main__":
    x, y = [1, 4, 8, 10], [2, 3, 9]
    merge_sorted(x, y)
    print(x, y)  # [1, 2, 3, 4] [8, 9, 10]
