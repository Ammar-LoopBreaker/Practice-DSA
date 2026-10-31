# How to find the smallest divisor given a threshold?
def smallest_divisor(nums, threshold):
    if not nums: return 1
    def s(d): return sum((n+d-1)//d for n in nums)
    l, r = 1, max(nums)
    while l < r:
        m = (l+r)//2
        l, r = (m, r) if s(m) <= threshold else (l, m+1)
    return l
def smallest_divisor_with_details(nums, threshold):
    d = smallest_divisor(nums, threshold)
    return d, sum((n+d-1)//d for n in nums)
if __name__=="__main__":
    tc=[([1,2,5,9],6),([2,3,5,7,11],11),([19],5),([1,2,3,4,5],5),([1,2,3,4,5],10),([1,2,3,4,5],15),([1,2,3,4,5],20),([2,3,5,7,11,13,17,19],100),([1000000],1000000),([1000000],1)]
    for i,(nums,th) in enumerate(tc):
        div=smallest_divisor(nums,th);_,tot=smallest_divisor_with_details(nums,th)
        print(f"Test {i+1}: nums={nums}, threshold={th}")
        print(f"  Divisor: {div} Sum: {tot}")
        if nums:
            expected_div=div
            actual_sum=sum((n+expected_div-1)//expected_div for n in nums)
            ok=actual_sum<=th
            if expected_div>1:
                prev_sum=sum((n+expected_div-2)//(expected_div-1) for n in nums)
                ok=ok and prev_sum>th
            print(f"  Correct: {'✓' if ok else '✗'}")
        else:
            print(f"  Correct: ✓" if div==1 else "  Incorrect: ✗")
        print()