# Question: Rotate an N x N matrix by 90 degrees clockwise.
# Example: [[1,2,3],[4,5,6],[7,8,9]] -> [[7,4,1],[8,5,2],[9,6,3]]
"""Rotate an N x N matrix 90 degrees clockwise."""


def rotate_matrix(matrix: list) -> list:
    """Transpose with zip, then reverse each row (done in one comprehension)."""
    matrix[:] = [list(row)[::-1] for row in zip(*matrix)]
    return matrix


if __name__ == "__main__":
    print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
