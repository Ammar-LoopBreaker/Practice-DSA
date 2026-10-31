# Question: If a matrix element is 0, set its entire row and column to 0.
# Example: [[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]
"""Set Matrix Zeroes: zero out the row and column of every 0."""


def set_matrix_zeroes(matrix: list) -> list:
    """Record zero rows/cols first, then blank them. O(m*n) time, O(m+n) space."""
    rows = {i for i, row in enumerate(matrix) if 0 in row}
    cols = {j for row in matrix for j, v in enumerate(row) if v == 0}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    print(set_matrix_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
