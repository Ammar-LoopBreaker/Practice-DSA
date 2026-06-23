'''Given an integer N, print the following pattern 
This pattern prints a right-angled triangle of alphabets where each row contains the same character repeatedly. 
The character printed in row i is 'A' + i'''

class Solution:
    def pattern16(self, N):
        for i in range(N):
            ch = chr(65 + i)

            for j in range(i + 1):
                print(ch, end=" ")

            print()

sol = Solution()
N = 5
sol.pattern16(N)