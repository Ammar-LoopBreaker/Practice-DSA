'''Given an integer N, print the following pattern
We always use nested loops for printing the patterns. For the outer loop, we count the number of lines/rows and loop for them.
Next, for the inner loop, we focus on the number of columns and somehow connect them to the rows by forming a logic such that for each row we get the required number of columns to be printed.
We print the ‘*’ inside the inner loop'''


class Solution:
    def halfDiamond(self, N):
        for i in range(1, N + 1):
            print("* " * i)

        for i in range(N - 1, 0, -1):
            print("* " * i)

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.halfDiamond(N)