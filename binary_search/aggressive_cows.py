# How to solve the Aggressive Cows problem?
def aggressive_cows(stalls, k):
    stalls.sort()
    def can_place(d):
        c=1;l=stalls[0]
        for s in stalls[1:]:
            if s-l>=d:
                c+=1;l=s
                if c>=k:return True
        return False
    lo,hi=1,stalls[-1]-stalls[0]
    while lo<=hi:
        mid=(lo+hi)//2
        if can_place(mid):lo=mid+1
        else:hi=mid-1
    return hi
if __name__=="__main__":
    tc=[([1,2,4,8,9],3),([1,2,3,4,5,6,7,8,9,10],3),([1,2,3,4,5],2),([1,2,3,4,5,6],3),([1,2,3,4,5,6,7,8,9,10],4),([1,2,3,4,5,6,7,8,9,10],5),([1,2,3,4,5,6,7,8,9,10],1),([1,2,3,4,5,6,7,8,9,10],10),([4,2,1,3,6],2),([5,17,100,11],2),([1,3,5,7,9,11,13,15],3),([1,3,5,7,9,11,13,15],4)]
    for i,(stalls,k) in enumerate(tc):
        res=aggressive_cows(stalls,k)
        print(f"Test {i+1}: stalls={stalls}, k={k} -> {res}")