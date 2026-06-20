'''Given an integer N, print the following pattern
In this pattern, we form a pyramid of stars. Each row contains
(N - i - 1) spaces on the left (to center align the stars),
(2 * i + 1) stars in the middle,
(N - i - 1) spaces on the right'''

class Solution:
    def pattern7(self, N):
        for i in range(N):
            for j in range(N - i - 1):
                print(" ", end="")

            for j in range(2 * i + 1):
                print("*", end="")

            for j in range(N - i - 1):
                print(" ", end="")

            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern7(N)