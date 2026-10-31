# Question: Return the indices of two numbers in the array that add up to the target.
# Example: [2, 7, 11, 15], target=9 -> [0, 1]
"""Two Sum: O(n) time with a hash map."""


def two_sum(nums: list, target: int) -> list:
    """Return indices of two numbers adding to target, or [] if none."""
    seen = {}                               # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:              # complement already seen
            return [seen[target - x], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
