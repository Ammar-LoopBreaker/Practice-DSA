# Question: Find all unique quadruplets in the array that add up to the target.
# Example: [1, 0, -1, 0, -2, 2], target=0 -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""4Sum: all unique quadruplets summing to target. O(n^3)."""


def four_sum(nums: list, target: int) -> list:

    nums, res, n = sorted(nums), [], len(nums)
    for i in range(n - 3):
        if i and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            lo, hi = j + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[j] + nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    res.append([nums[i], nums[j], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
    return res


if __name__ == "__main__":
    print(four_sum([1, 0, -1, 0, -2, 2], 0))
    # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
