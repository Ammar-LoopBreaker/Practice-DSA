# Question: Find the union and the intersection of two sorted arrays.
# Example: [1, 2, 2, 3] and [2, 4] -> union [1, 2, 3, 4]
"""Union and intersection of two sorted arrays using two pointers."""


def union_sorted(a: list, b: list) -> list:
    """Sorted union without duplicates."""
    i = j = 0
    res = []
    while i < len(a) or j < len(b):
        if j >= len(b) or (i < len(a) and a[i] <= b[j]):
            x, i = a[i], i + 1
        else:
            x, j = b[j], j + 1
        if not res or res[-1] != x:         # skip duplicates
            res.append(x)
    return res


def intersection_sorted(a: list, b: list) -> list:
    """Common elements (with multiplicity)."""
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            res.append(a[i])
            i, j = i + 1, j + 1
    return res


if __name__ == "__main__":
    print(union_sorted([1, 2, 2, 3], [2, 4]))         # [1, 2, 3, 4]
    print(intersection_sorted([1, 2, 2, 3], [2, 2]))  # [2, 2]
