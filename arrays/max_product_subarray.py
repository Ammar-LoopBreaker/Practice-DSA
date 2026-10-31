# Question: Find the contiguous subarray with the largest product.
# Example: [2, 3, -2, 4] -> 6
"""Maximum product subarray: O(n) time, O(1) space."""


def max_product_subarray(nums: list) -> int:
    """Track both max and min product ending here (a negative can flip them)."""
    best = cur_max = cur_min = nums[0]
    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best


if __name__ == "__main__":
    print(max_product_subarray([2, 3, -2, 4]))  # 6
