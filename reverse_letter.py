class Solution:
    def pattern15(self, N):
        for i in range(N):
            for j in range(N - i):
                print(chr(65 + j), end=" ")

            print()

sol = Solution()
N = 5
sol.pattern15(N)