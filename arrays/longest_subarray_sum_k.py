# Question: Find the length of the longest subarray whose sum equals k.
# Example: [10, 5, 2, 7, 1, 9], k=15 -> 4
"""Longest subarray with sum k (works with negatives) using prefix sums."""


def longest_subarray_sum_k(arr: list, k: int) -> int:
    """Store first index of each prefix sum; look up (prefix - k)."""
    first = {0: -1}                         # prefix sum -> earliest index
    prefix = best = 0
    for i, x in enumerate(arr):
        prefix += x
        if prefix - k in first:
            best = max(best, i - first[prefix - k])
        first.setdefault(prefix, i)         # keep earliest occurrence only
    return best


if __name__ == "__main__":
    print(longest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15))  # 4
