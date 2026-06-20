'''Given an integer N, print the following pattern
The goal is to print a pattern of alphabets where each row starts with a letter that is progressively closer to 'A' as we move down. 
The last column always has the letter 'A' + N - 1, and in each row, 
we print an increasing sequence from a starting letter up to this last letter.
'''

class Solution:
    def pattern18(self, N):
        for i in range(N):
            for ch in range(ord('A') + N - 1 - i, ord('A') + N):
                print(chr(ch), end=" ")

            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern18(N)