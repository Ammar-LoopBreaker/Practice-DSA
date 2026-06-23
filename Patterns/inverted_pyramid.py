'''Given an integer N, print the following pattern
This pattern looks similar to an inverted right-angled triangle, 
but instead of stars, we print numbers. 
Each row starts from 1 and continues up to N - i, where i is the current row index. 
Thus, the number of elements decreases with each row, creating an inverted triangle of numbers..'''

class Solution:
    def pattern6(self, N):
        for i in range(N):
            for j in range(N, i, -1):
                print(N - j + 1, end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern6(N)