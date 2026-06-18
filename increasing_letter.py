class Solution:
    def pattern14(self, N):
        for i in range(N):
            for j in range(i + 1):
                print(chr(65 + j), end=" ")

            print()

sol = Solution()
N = 5
sol.pattern14(N)