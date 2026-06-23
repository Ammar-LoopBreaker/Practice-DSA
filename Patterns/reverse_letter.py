'''given an integer N, print the following pattern
This pattern prints rows of decreasing-length alphabet sequences starting from 'A'. 
In the first row, it prints from 'A' to 'E', 
in the second from 'A' to 'D', and so on, reducing by one letter each row.'''

class Solution:
    def pattern15(self, N):
        for i in range(N):
            for j in range(N - i):
                print(chr(65 + j), end=" ")

            print()

sol = Solution()
N = 5
sol.pattern15(N)