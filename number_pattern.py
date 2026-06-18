class Solution:
    def pattern22(self, n):
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):

                top = i
                left = j
                bottom = (2 * n - 2) - i
                right = (2 * n - 2) - j

                minDist = min(top, bottom, left, right)

                print(n - minDist, end=" ")

            print()


if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern22(N)