class Solution:
    def pattern16(self, N):
        for i in range(N):
            ch = chr(65 + i)

            for j in range(i + 1):
                print(ch, end=" ")

            print()

sol = Solution()
N = 5
sol.pattern16(N)