# How to find how many times an array is rotated?
def find_rotation_count(nums):
    if not nums:
        return 0
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return l
def find_rotation_count_with_duplicates(nums):
    if not nums:
        return 0
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] < nums[r]:
            r = m
        else:
            r -= 1
    return l
def is_array_rotated(nums):
    return len(nums) > 1 and nums[0] > nums[-1]
if __name__ == "__main__":
    tc = [[3,4,5,1,2],[4,5,6,7,0,1,2],[11,13,15,17],[2,1],[1],[],[1,2,3,4,5],[5,1,2,3,4],[3,1,2],[2,3,1],[4,5,6,7,8,9,1],[4,5,6,7,8,9,1,2],[6,7,8,9,10,1,2,3,4,5]]
    print("=== Rotation Count (No Duplicates) ===")
    for i, nums in enumerate(tc):
        cnt = find_rotation_count(nums)
        rot = is_array_rotated(nums)
        print(f"Test {i+1}: {nums} -> rotations={cnt}, is_rotated={rot}")
        if nums:
            ok = cnt == nums.index(min(nums)) if nums else True
            print(f"  Correct: {'✓' if ok else '✗'}")
        else:
            print(f"  Correct: ✓" if cnt == 0 else "  Incorrect: ✗")
        print()
    tc_dup = [[2,2,2,0,1],[2,2,2,2,2,2],[3,3,1,3],[1,1,1,0,1],[1,0,1,1,1],[10,1,10,10,10],[10,10,10,1,10],[3,3,3,3,3,3,3,3,3],[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1],[],[1]]
    print("=== Rotation Count (With Duplicates) ===")
    for i, nums in enumerate(tc_dup):
        cnt = find_rotation_count_with_duplicates(nums)
        print(f"Test {i+1}: {nums} -> {cnt}")
        if nums:
            ok = cnt == nums.index(min(nums))
            print(f"  Correct: {'✓' if ok else '✗'}")
        else:
            print(f"  Correct: ✓" if cnt == 0 else "  Incorrect: ✗")
        print()