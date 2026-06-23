'''Given an integer N, print the following pattern
This is one of the simplest star patterns. We need to form a right-angled triangle 
where the number of stars in each row increases line by line. 
Row i contains exactly i + 1 stars.'''


class Solution:
    def pattern2(self, N):
        for i in range(N):
            print("* " * (i + 1))

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern2(N)