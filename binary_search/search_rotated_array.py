# Question: Search for a target in a rotated sorted array of distinct values.
# Example: [4,5,6,7,0,1,2], target=0 -> 4
"""Search in a rotated sorted array (distinct values): O(log n)."""


def search_rotated(nums: list, target) -> int:
    """At every step, at least one half is sorted; check if target lies in it."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                       # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                           # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
