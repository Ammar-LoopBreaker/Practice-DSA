# Question: Sort an array containing only 0s, 1s and 2s without using a sorting function.
# Example: [2, 0, 2, 1, 1, 0] -> [0, 0, 1, 1, 2, 2]
"""Sort an array of 0s, 1s, 2s: Dutch National Flag, one pass, O(1) space."""


def sort_012(nums: list) -> list:
    """Maintain regions: [0,low) zeros, [low,mid) ones, (high,end] twos."""
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low, mid = low + 1, mid + 1
        elif nums[mid] == 1:
            mid += 1
        else:                               # 2: swap to the back, don't advance mid
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


if __name__ == "__main__":
    print(sort_012([2, 0, 2, 1, 1, 0]))  # [0, 0, 1, 1, 2, 2]
