def print_numbers(n):
   
    if n == 0:
        return
    print(n, end=" ")
    print_numbers(n - 1)
n = 10
print_numbers(n)