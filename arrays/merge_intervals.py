# Question: Merge all overlapping intervals.
# Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
"""Merge overlapping intervals: O(n log n)."""


def merge_intervals(intervals: list) -> list:
    """Sort by start, then extend the last interval whenever the next overlaps."""
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:       # overlap
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # [[1, 6], [8, 10], [15, 18]]
