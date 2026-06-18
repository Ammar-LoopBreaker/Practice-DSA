class Solution:
    def halfDiamond(self, N):
        for i in range(1, N + 1):
            print("* " * i)

        for i in range(N - 1, 0, -1):
            print("* " * i)

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.halfDiamond(N)