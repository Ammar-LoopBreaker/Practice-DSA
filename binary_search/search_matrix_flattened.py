# Question: Search a target in a matrix where each row is sorted and each row starts after the previous row ends.
# Example: target=3 -> True, target=13 -> False
"""Search a 2D matrix where rows are sorted and each row starts after the previous ends."""


def search_matrix(matrix: list, target) -> bool:
    """Treat the m x n matrix as one sorted array of length m*n. O(log(m*n))."""
    if not matrix or not matrix[0]:
        return False
    n = len(matrix[0])
    lo, hi = 0, len(matrix) * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]     # map 1D index back to (row, col)
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


if __name__ == "__main__":
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(search_matrix(m, 3), search_matrix(m, 13))  # True False
