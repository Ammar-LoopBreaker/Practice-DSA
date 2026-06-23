'''Given an integer N, print the following pattern 
The pattern consists of two mirrored halves forming an hourglass-like shape made of stars (*). 
The upper half starts with N stars on both sides and gradually reduces, 
while the lower half starts with 1 star on both sides and gradually increases. 
Spaces in between adjust accordingly to maintain symmetry
'''

class Solution:
    def pattern19(self, N):
        iniS = 0

        for i in range(N):
            print("*" * (N - i), end="")
            print(" " * iniS, end="")
            print("*" * (N - i))

            iniS += 2

        iniS = 2 * N - 2

        for i in range(1, N + 1):
            print("*" * i, end="")
            print(" " * iniS, end="")
            print("*" * i)

            iniS -= 2

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern19(N)
    