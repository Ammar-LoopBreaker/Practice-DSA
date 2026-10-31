# How to solve the Book Allocation problem?
def book_allocation(pages, m):
    if not pages or m <= 0:
        return -1
    if m > len(pages):
        return -1
    def can_allocate(max_pages):
        students = 1
        cur = 0
        for p in pages:
            if cur + p > max_pages:
                students += 1
                cur = p
                if students > m:
                    return False
            else:
                cur += p
        return students <= m
    l, r = max(pages), sum(pages)
    while l < r:
        mid = (l + r) // 2
        if can_allocate(mid):
            r = mid
        else:
            l = mid + 1
    return l
if __name__ == "__main__":
    tc = [([12, 34, 67, 90], 2), ([12, 34, 67, 90], 1), ([12, 34, 67, 90], 4), ([12, 34, 67, 90], 3), ([5, 17, 100, 11], 2), ([5, 17, 100, 11], 1), ([5, 17, 100, 11], 4), ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), ([1, 2, 3, 4, 5], 3), ([10, 20, 30, 40], 2), ([10, 20, 30, 40], 3), ([10, 20, 30, 40], 4), ([100], 1), ([100], 2)]
    for i, (pages, m) in enumerate(tc):
        res = book_allocation(pages, m)
        print(f"Test {i+1}: pages={pages}, m={m} -> {res}")
        if res != -1:
            students = 1
            cur = 0
            for p in pages:
                if cur + p > res:
                    students += 1
                    cur = p
                else:
                    cur += p
            ok = students <= m
            if res > max(pages):
                students2 = 1
                cur2 = 0
                for p in pages:
                    if cur2 + p > res - 1:
                        students2 += 1
                        cur2 = p
                    else:
                        cur2 += p
                ok2 = students2 > m
            else:
                ok2 = True
            print(f"  Correct: {'✓' if ok and ok2 else '✗'}")
        else:
            print(f"  Correct: ✓" if m <= 0 or not pages or m > len(pages) else "  Incorrect: ✗")
        print()