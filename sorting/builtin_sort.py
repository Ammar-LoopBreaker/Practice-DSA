# Question: Show how to sort in Python with sorted(), list.sort(), key= and reverse=.
# Example: [5, 2, 9, 1] -> [1, 2, 5, 9]
"""Python's built-in sorting (Timsort): O(n log n), stable."""


def builtin_sort_demo() -> None:
    """Show sorted(), list.sort(), key= and reverse=."""
    nums = [5, 2, 9, 1]
    print(sorted(nums))                      # new list: [1, 2, 5, 9]
    nums.sort(reverse=True)                  # in place:  [9, 5, 2, 1]
    print(nums)

    words = ["banana", "fig", "apple"]
    print(sorted(words, key=len))            # by length: ['fig', 'apple', 'banana']

    pairs = [(1, "b"), (2, "a"), (1, "a")]
    print(sorted(pairs, key=lambda p: (p[0], p[1])))  # multi-key sort


if __name__ == "__main__":
    builtin_sort_demo()
