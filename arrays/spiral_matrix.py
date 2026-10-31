# Question: Return the elements of a matrix in spiral order.
# Example: [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
"""Spiral traversal of a matrix."""


def spiral_order(matrix: list) -> list:
    """Peel off the top row, then rotate the rest counter-clockwise; repeat."""
    m = [row[:] for row in matrix]          # copy so the input isn't mutated
    res = []
    while m:
        res += m.pop(0)                     # take the top row
        m = [list(col) for col in zip(*m)][::-1]  # rotate remaining counter-clockwise
    return res


if __name__ == "__main__":
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # [1, 2, 3, 6, 9, 8, 7, 4, 5]
