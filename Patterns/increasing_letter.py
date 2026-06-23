'''Given an integer N, print the following pattern
This pattern prints letters in a triangular format where each row starts from 'A' and goes up to a certain alphabet depending on the row number. 
The idea is to print increasing sequences of alphabets in each row.'''

class Solution:
    def pattern14(self, N):
        for i in range(N):
            for j in range(i + 1):
                print(chr(65 + j), end=" ")

            print()

sol = Solution()
N = 5
sol.pattern14(N)