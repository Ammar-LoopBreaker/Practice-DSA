# How to find minimum in rotated sorted array?
def find_min(nums):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]
def find_min_with_duplicates(nums):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] < nums[r]:
            r = m
        else:
            r -= 1
    return nums[l]
def find_min_index(nums):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return l
if __name__ == "__main__":
    tc = [[3,4,5,1,2],[4,5,6,7,0,1,2],[11,13,15,17],[2,1],[1],[],[1,2,3,4,5],[5,1,2,3,4],[3,1,2],[2,3,1],[4,5,6,7,8,9,1],[4,5,6,7,8,9,1,2]]
    print("=== Find Minimum (No Duplicates) ===")
    for i, nums in enumerate(tc):
        res = find_min(nums)
        idx = find_min_index(nums)
        print(f"Test {i+1}: {nums} -> min={res}, index={idx}")
        if nums:
            ok = res == min(nums) and idx == nums.index(min(nums))
            print(f"  Correct: {'✓' if ok else '✗'}")
        else:
            print(f"  Correct: ✓" if res == -1 else "  Incorrect: ✗")
        print()
    tc_dup = [[2,2,2,0,1],[2,2,2,2,2,2],[3,3,1,3],[1,1,1,0,1],[1,0,1,1,1],[10,1,10,10,10],[10,10,10,1,10],[3,3,3,3,3,3,3,3,3],[],[1]]
    print("=== Find Minimum (With Duplicates) ===")
    for i, nums in enumerate(tc_dup):
        res = find_min_with_duplicates(nums)
        print(f"Test {i+1}: {nums} -> {res}")
        if nums:
            ok = res == min(nums)
            print(f"  Correct: {'✓' if ok else '✗'}")
        else:
            print(f"  Correct: ✓" if res == -1 else "  Incorrect: ✗")
        print()