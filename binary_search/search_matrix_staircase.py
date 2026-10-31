# Question: Search a target in a matrix where every row and every column is sorted.
# Example: target=5 -> True, target=20 -> False
"""Search a matrix with rows sorted and columns sorted (rows NOT chained)."""


def search_matrix_ii(matrix: list, target) -> bool:
    """Start at the top-right corner and walk left/down. O(m + n)."""
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        val = matrix[r][c]
        if val == target:
            return True
        if val > target:
            c -= 1                          # everything below in this column is bigger
        else:
            r += 1                          # everything left in this row is smaller
    return False


if __name__ == "__main__":
    m = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    print(search_matrix_ii(m, 5), search_matrix_ii(m, 20))  # True False
