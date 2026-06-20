''' Given an integer N, print the following pattern
We need to print a right-angled triangle where each row contains numbers starting from 1 up to the row number. 
So, the first row has 1, the second row has 1 2, the third row has 1 2 3, and so on until N.'''


class Solution:
    def pattern3(self, N):
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern3(N)