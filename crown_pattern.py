class Solution:
    def pattern12(self, N):
        spaces = 2 * (N - 1)

        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(j, end="")

            for j in range(1, spaces + 1):
                print(" ", end="")

            for j in range(i, 0, -1):
                print(j, end="")

            print()

            spaces -= 2

sol = Solution()
N = 5
sol.pattern12(N)