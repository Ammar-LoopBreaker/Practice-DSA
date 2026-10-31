# Question: Count pairs (i < j) where arr[i] > arr[j].
# Example: [5, 3, 2, 4, 1] -> 8
"""Count inversions (i < j and arr[i] > arr[j]) with merge sort: O(n log n)."""


def count_inversions(arr: list) -> int:

    def sort(a: list) -> tuple:
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, x = sort(a[:mid])
        right, y = sort(a[mid:])
        merged, count, i, j = [], x + y, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                count += len(left) - i      # all remaining left items are larger
        return merged + left[i:] + right[j:], count

    return sort(arr)[1]


if __name__ == "__main__":
    print(count_inversions([5, 3, 2, 4, 1]))  # 8
