class Solution:
    def pattern2(self, N):
        for i in range(N):
            print("* " * (i + 1))

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern2(N)