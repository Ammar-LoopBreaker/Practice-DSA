'''Given an integer N, print the following pattern
We need to print a square of size n × n but only with stars on the border, 
leaving the inner cells as spaces. 
This creates a "hollow square" effect.'''

class Solution:
    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern21(N)