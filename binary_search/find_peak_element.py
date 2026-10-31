# How to find a peak element?
def find_peak_element(nums):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[m + 1]:
            r = m
        else:
            l = m + 1
    return l
def find_peak_element_recursive(nums, l=0, r=None):
    if r is None:
        r = len(nums) - 1
    if l > r:
        return -1
    if l == r:
        return l
    m = (l + r) // 2
    if nums[m] > nums[m + 1]:
        return find_peak_element_recursive(nums, l, m)
    else:
        return find_peak_element_recursive(nums, m + 1, r)
def find_all_peaks(nums):
    if not nums:
        return []
    return [i for i in range(len(nums)) if (i==0 or nums[i]>nums[i-1]) and (i==len(nums)-1 or nums[i]>nums[i+1])]
if __name__ == "__main__":
    tc = [[1,2,3,1],[1,2,1,3,5,6,4],[1],[1,2],[2,1],[1,2,3,4,5],[5,4,3,2,1],[1,3,2,1,2],[2,2,2],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],[],[1,2,3,4,5,6,5,4,3,2,1]]
    for i, nums in enumerate(tc):
        idx = find_peak_element(nums)
        val = nums[idx] if idx != -1 else None
        allp = find_all_peaks(nums)
        print(f"Test {i+1}: {nums}")
        print(f"  Peak index: {idx}")
        if idx != -1:
            print(f"  Peak value: {val}")
        print(f"  All peaks: {allp}")
        if nums:
            if idx != -1:
                left_ok = idx == 0 or nums[idx] > nums[idx-1]
                right_ok = idx == len(nums)-1 or nums[idx] > nums[idx+1]
                ok = left_ok and right_ok
                print(f"  Correct: {'✓' if ok else '✗'}")
            else:
                print("  Correct: ✗")
        else:
            print(f"  Correct: ✓" if idx == -1 else "  Incorrect: ✗")
        print()