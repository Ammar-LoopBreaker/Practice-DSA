# Question: Given daily stock prices, find the maximum profit from one buy and one later sell.
# Example: [7, 1, 5, 3, 6, 4] -> 5
"""Best Time to Buy and Sell Stock (one transaction)."""


def max_profit(prices: list) -> int:
    """Track the lowest price so far and the best profit if selling today."""
    lowest, best = float("inf"), 0
    for p in prices:
        lowest = min(lowest, p)
        best = max(best, p - lowest)
    return best


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
