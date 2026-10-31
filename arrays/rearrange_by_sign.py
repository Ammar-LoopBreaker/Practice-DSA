# Question: Rearrange the array so positive and negative numbers alternate, starting with positive.
# Example: [3, 1, -2, -5, 2, -4] -> [3, -2, 1, -5, 2, -4]
"""Rearrange an array so positives and negatives alternate (equal counts)."""


def rearrange_by_sign(nums: list) -> list:
    """Keep relative order within each sign; start with a positive."""
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]
    res = []
    for p, n in zip(pos, neg):
        res += [p, n]
    return res


if __name__ == "__main__":
    print(rearrange_by_sign([3, 1, -2, -5, 2, -4]))  # [3, -2, 1, -5, 2, -4]
