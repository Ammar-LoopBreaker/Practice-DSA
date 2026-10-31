# Question: Remove duplicates from a sorted array in place and return the count of unique elements.
# Example: [1, 1, 2, 2, 3] -> 3, array starts [1, 2, 3]
"""Remove duplicates from a sorted array in place (two pointers)."""


def remove_duplicates(nums: list) -> int:
    """Compact unique values to the front; return the count of unique values."""
    if not nums:
        return 0
    k = 1                                   # next write position
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:          # new distinct value
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == "__main__":
    a = [1, 1, 2, 2, 3]
    k = remove_duplicates(a)
    print(k, a[:k])  # 3 [1, 2, 3]
