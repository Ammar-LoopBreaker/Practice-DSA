# Question: Find all unique triplets in the array that add up to zero.
# Example: [-1, 0, 1, 2, -1, -4] -> [[-1,-1,2],[-1,0,1]]
"""3Sum: all unique triplets summing to zero. O(n^2)."""


def three_sum(nums: list) -> list:
    """Sort, fix one number, then use two pointers for the other two."""
    nums, res = sorted(nums), []
    for i in range(len(nums) - 2):
        if i and nums[i] == nums[i - 1]:    # skip duplicate anchors
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:  # skip duplicates
                    lo += 1
    return res


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
