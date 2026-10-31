# Question: Generate the first n rows of Pascal's Triangle.
# Example: n=5 -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""Pascal's Triangle."""


def pascals_triangle(num_rows: int) -> list:
    """Each inner value is the sum of the two values above it."""
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    print(pascals_triangle(5))
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
