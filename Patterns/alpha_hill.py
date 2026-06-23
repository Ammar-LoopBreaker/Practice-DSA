'''Given an integer N, print the following pattern
The pattern should contain N rows. In each row, 
characters are printed in increasing alphabetical order starting from A up to a peak character and then in decreasing order, 
forming a symmetric hill shape.'''

def pattern17(N):
    for i in range(N):

        print(" " * (N - i - 1), end="")

        ch = ord('A')
        breakpoint = (2 * i + 1) // 2

        for j in range(1, 2 * i + 2):
            print(chr(ch), end="")

            if j <= breakpoint:
                ch += 1
            else:
                ch -= 1

        print()

if __name__ == "__main__":
    N = 5
    pattern17(N)