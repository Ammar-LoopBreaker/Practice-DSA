class Solution:
    def pattern18(self, N):
        for i in range(N):
            for ch in range(ord('A') + N - 1 - i, ord('A') + N):
                print(chr(ch), end=" ")

            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern18(N)