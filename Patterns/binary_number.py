'''Given an integer N, print the following pattern
This pattern prints alternating 1s and 0s in each row, starting with 1 on even-indexed rows and 0 on odd-indexed rows. 
The value alternates after each print using basic toggling logic.'''

class Solution:
    def pattern11(self, N):
        for i in range(N):
            if i % 2 == 0:
                start = 1
            else:
                start = 0

            for j in range(i + 1):
                print(start, end="")
                start = 1 - start

            print()

sol = Solution()
N = 5
sol.pattern11(N)