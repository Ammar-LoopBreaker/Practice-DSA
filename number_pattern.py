'''Given an integer N, print the following pattern
We need to print a square matrix of size (2 * n - 1) × (2 * n - 1). 
The outermost border should contain n, the next inner layer n-1, then n-2, 
and so on until the center which contains 1. This creates a concentric square pattern.

'''

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