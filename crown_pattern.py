'''Given an integer N, print the following pattern
 This pattern prints a mirrored sequence of numbers on both sides with spaces in the center. 
 The outer digits increase and decrease symmetrically, 
 while the center gap shrinks with each row, forming a diamond-like structure across rows.'''

class Solution:
    def pattern12(self, N):
        spaces = 2 * (N - 1)

        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(j, end="")

            for j in range(1, spaces + 1):
                print(" ", end="")

            for j in range(i, 0, -1):
                print(j, end="")

            print()

            spaces -= 2

sol = Solution()
N = 5
sol.pattern12(N)