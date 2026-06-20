'''Given an integer N, print the following pattern 
This pattern prints a continuous sequence of increasing numbers, 
arranged row by row in a triangular structure. Each row has one more number than the previous, 
and the values increment consecutively throughout the triangle.'''

class Solution:
    def pattern13(self, N):
        num = 1

        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1

            print()

sol = Solution()
N = 5
sol.pattern13(N)