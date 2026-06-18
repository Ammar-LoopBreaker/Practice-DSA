def print_name(name, n):
    if n == 0:
        return

    print(name)
    print_name(name, n - 1)

name = "Ashish"
n = 5

print_name(name, n)