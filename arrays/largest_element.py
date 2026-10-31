# Question: Find the largest element in an array.
# Example: [3, 2, 1, 5, 2] -> 5
"""Find the largest element: O(n) time, O(1) space."""


def largest_element(arr: list):
    """Return the maximum value in a non-empty list."""
    if not arr:
        raise ValueError("array is empty")
    largest = arr[0]
    for x in arr[1:]:
        if x > largest:
            largest = x
    return largest


if __name__ == "__main__":
    print(largest_element([3, 2, 1, 5, 2]))  # 5
