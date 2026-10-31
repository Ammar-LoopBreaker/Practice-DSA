# Question: Count the subarrays whose XOR is equal to k.
# Example: [4, 2, 2, 6, 4], k=6 -> 4
"""Count subarrays whose XOR equals k: O(n) with prefix XOR + hash map."""


def count_subarrays_xor_k(arr: list, k: int) -> int:
    """If prefix ^ k was seen before, a subarray ending here has XOR k."""
    seen = {0: 1}                           # prefix xor -> occurrences
    prefix = count = 0
    for x in arr:
        prefix ^= x
        count += seen.get(prefix ^ k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


if __name__ == "__main__":
    print(count_subarrays_xor_k([4, 2, 2, 6, 4], 6))  # 4
