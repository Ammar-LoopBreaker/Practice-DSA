'''Given an integer N, print the following pattern.
The task is to print a square pattern of stars. Since the number of rows and columns are equal, we can use two nested loops:
the outer one for rows and the inner one for printing N stars per row.'''

class Solution:
    def pattern1(self, N):
        for i in range(N):
            for j in range(N):
                print("*", end=" ")
            print()

sol = Solution()
N = 5
sol.pattern1(N)