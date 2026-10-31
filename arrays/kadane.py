# Question: Find the contiguous subarray with the largest sum (Kadane's Algorithm).
# Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
"""Kadane's Algorithm: maximum subarray sum in O(n)."""


def kadane(arr: list) -> tuple:
    
    best = cur = arr[0]
    begin = lo = hi = 0
    for i in range(1, len(arr)):
        if cur < 0:                         # a negative prefix only hurts: restart
            cur, begin = arr[i], i
        else:
            cur += arr[i]
        if cur > best:
            best, lo, hi = cur, begin, i
    return best, arr[lo:hi + 1]


if __name__ == "__main__":
    print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # (6, [4, -1, 2, 1])
