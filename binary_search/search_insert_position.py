# How to search insert position in sorted array?
def search_insert_position(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l
def search_insert_position_recursive(nums, target, l=0, r=None):
    if r is None:
        r = len(nums)
    if l >= r:
        return l
    m = (l + r) // 2
    if nums[m] < target:
        return search_insert_position_recursive(nums, target, m + 1, r)
    else:
        return search_insert_position_recursive(nums, target, l, m)
def search_insert_position_linear(nums, target):
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)
def search_insert_position_using_bisect(nums, target):
    import bisect
    return bisect.bisect_left(nums, target)
def search_insert_position_with_result(nums, target):
    idx = search_insert_position(nums, target)
    f = idx < len(nums) and nums[idx] == target
    v = nums[idx] if idx < len(nums) else None
    return idx, f, v
if __name__ == "__main__":
    tc = [([1,3,5,6],5),([1,3,5,6],2),([1,3,5,6],7),([1,3,5,6],0),([1,3,5,6,8,10],6),([],5),([1],0),([1],2),([1,1,1,1,1],1),([1,2,4,4,4,5,7],4),([1,2,4,4,4,5,7],3),([1,2,4,4,4,5,7],6)]
    for i,(n,t) in enumerate(tc):
        it=search_insert_position(n,t)
        re=search_insert_position_recursive(n,t)
        li=search_insert_position_linear(n,t)
        bi=search_insert_position_using_bisect(n,t)
        idx,found,val=search_insert_position_with_result(n,t)
        print(f"Test {i+1}: nums={n}, target={t}")
        print(f"  It:{it} Re:{re} Li:{li} Bi:{bi} Res:{idx},{found},{val}")
        if it==re==li==bi==idx:
            if found:
                print(f"  Found at {idx}")
            else:
                print(f"  Insert at {idx}")
                if idx < len(n):
                    print(f"    Before {n[idx]}")
                else:
                    print("    At end")
            print("  All agree: ✓")
        else:
            print("  Methods disagree!")
        print()