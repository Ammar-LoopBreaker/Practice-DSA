class Solution:
    def pattern20(self, n):
        spaces = 2 * n - 2

        for i in range(1, 2 * n):
            stars = i

            if i > n:
                stars = 2 * n - i

            print("*" * stars, end="")
            print(" " * spaces, end="")
            print("*" * stars)

            if i < n:
                spaces -= 2
            else:
                spaces += 2


if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern20(N)