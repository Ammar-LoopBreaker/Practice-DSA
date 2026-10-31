# Question: Find all leaders: elements greater than or equal to every element on their right.
# Example: [10, 22, 12, 3, 0, 6] -> [22, 12, 6]
"""Leaders: elements greater than or equal to everything on their right."""


def leaders(arr: list) -> list:
    """Scan right to left keeping the running maximum."""
    res, max_right = [], float("-inf")
    for x in reversed(arr):
        if x >= max_right:
            res.append(x)
            max_right = x
    return res[::-1]                        # restore original order


if __name__ == "__main__":
    print(leaders([10, 22, 12, 3, 0, 6]))  # [22, 12, 6]
