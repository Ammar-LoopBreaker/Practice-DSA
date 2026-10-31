# Question: Rearrange the array into the next lexicographically greater permutation.
# Example: [1, 2, 3] -> [1, 3, 2]
"""Next lexicographic permutation, in place: O(n) time, O(1) space."""


def next_permutation(nums: list) -> list:
    """Rearrange to the next greater permutation (or the smallest if at the max)."""
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:   # find the first "dip" from the right
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:              # smallest value greater than nums[i]
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])      # make the suffix as small as possible
    return nums


if __name__ == "__main__":
    print(next_permutation([1, 2, 3]))  # [1, 3, 2]
    print(next_permutation([3, 2, 1]))  # [1, 2, 3]
