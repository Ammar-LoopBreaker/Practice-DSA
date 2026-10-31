# Question: In an array of 1..n, one number repeats and one is missing. Find both.
# Example: [3, 1, 2, 5, 3] -> repeating 3, missing 4
"""Find the repeating and missing numbers in an array of 1..n (one of each wrong)."""


def repeating_missing(arr: list) -> tuple:
    """Use sum and sum of squares: R-M = d, R^2-M^2 = s  =>  R+M = s/d."""
    n = len(arr)
    d = sum(arr) - n * (n + 1) // 2                          # R - M
    s = sum(x * x for x in arr) - n * (n + 1) * (2 * n + 1) // 6  # R^2 - M^2
    total = s // d                                           # R + M
    return (d + total) // 2, (total - d) // 2                # (repeating, missing)


if __name__ == "__main__":
    print(repeating_missing([3, 1, 2, 5, 3]))  # (3, 4)
