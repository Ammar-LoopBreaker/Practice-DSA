# How to compute integer square root using binary search?
def sqrt(x):
    if x < 2:
        return x
    l, r = 1, x // 2
    while l <= r:
        m = (l + r) // 2
        sq = m * m
        if sq == x:
            return m
        elif sq > x:
            r = m - 1
        else:
            l = m + 1
    return r
def sqrt_recursive(x, l=1, r=None):
    if r is None:
        r = x // 2 if x >= 2 else x
    if l > r:
        return r
    m = (l + r) // 2
    sq = m * m
    if sq == x:
        return m
    elif sq > x:
        return sqrt_recursive(x, l, m - 1)
    else:
        return sqrt_recursive(x, m + 1, r)
def sqrt_linear(x):
    if x < 2:
        return x
    i = 1
    while i * i <= x:
        i += 1
    return i - 1
if __name__ == "__main__":
    tc = [0,1,2,3,4,8,9,15,16,24,25,26,100,101,1000,1024,1025,2**30,2**31-1]
    for i,x in enumerate(tc):
        it=sqrt(x)
        re=sqrt_recursive(x)
        li=sqrt_linear(x)
        print(f"Test {i+1}: x={x}")
        print(f"  BS:{it} Rec:{re} Lin:{li}")
        if it==re==li:
            if it*it <= x < (it+1)*(it+1):
                print("  Correct: ✓")
            else:
                print("  Incorrect: ✗")
        else:
            print("  Methods disagree!")
        print()