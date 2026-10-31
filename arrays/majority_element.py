# Question: Find the element that appears more than n/2 times in the array.
# Example: [2, 2, 1, 1, 1, 2, 2] -> 2
"""Majority element (> n/2 times) with Boyer-Moore voting."""


def majority_element(nums: list):
    """Return the majority element, or None if there isn't one."""
    cand, count = None, 0
    for x in nums:
        if count == 0:
            cand = x
        count += 1 if x == cand else -1     # matching votes add, others cancel
    return cand if nums.count(cand) > len(nums) // 2 else None  # verify


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
