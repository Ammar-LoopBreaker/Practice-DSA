# Question: Count pairs (i < j) where nums[i] > 2 * nums[j].
# Example: [1, 3, 2, 3, 1] -> 2
"""Reverse Pairs: count (i < j) with nums[i] > 2 * nums[j]. O(n log n)."""


def reverse_pairs(nums: list) -> int:
    """Merge-sort variant: count cross pairs before merging the halves."""
    def sort(a: list) -> tuple:
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, x = sort(a[:mid])
        right, y = sort(a[mid:])
        count, j = x + y, 0
        for v in left:                      # left ascending -> j only moves forward
            while j < len(right) and v > 2 * right[j]:
                j += 1
            count += j
        return sorted(left + right), count  # Timsort merges two sorted runs in O(n)

    return sort(nums)[1]


if __name__ == "__main__":
    print(reverse_pairs([1, 3, 2, 3, 1]))  # 2
