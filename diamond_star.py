class Solution:
    def erect_pyramid(self, N):
        for i in range(N):
            print(" " * (N - i - 1), end="")
            print("*" * (2 * i + 1), end="")
            print(" " * (N - i - 1))
    
    def inverted_pyramid(self, N):
        for i in range(N):
            print(" " * i, end="")
            print("*" * (2 * N - (2 * i + 1)), end="")
            print(" " * i)

if __name__ == "__main__":
    N = 5
    obj = Solution()
    obj.erect_pyramid(N)
    obj.inverted_pyramid(N)