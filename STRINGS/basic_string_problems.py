# How to solve basic string problems?
def rs(s):return s[::-1]
def rip(s):return''.join(reversed(s))
def rtp(s):
    c=list(s);l,r=0,len(c)-1
    while l<r:c[l],c[r]=c[r],c[l];l+=1;r-=1
    return''.join(c)
def ip(s):
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:return False
        l+=1;r-=1
    return True
def ips(s):return s==s[::-1]
def ipic(s):
    f=''.join(c.lower()for c in s if c.isalnum())
    l,r=0,len(f)-1
    while l<r:
        if f[l]!=f[r]:return False
        l+=1;r-=1
    return True
def lon(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2:return s[:i+1]
    return""
def lcp(s):
    if not s:return""
    p=s[0]
    for x in s[1:]:
        while x[:len(p)]!=p and p:p=p[:-1]
        if not p:break
    return p
def iso(s,t):
    if len(s)!=len(t):return False
    d={}
    for a,b in zip(s,t):
        if a in d:
            if d[a]!=b:return False
        else:d[a]=b
    return len(d)==len(set(s))==len(set(t))
def rot(s1,s2):return len(s1)==len(s2) and s2 in s1+s1
def ana(s,t):return sorted(s)==sorted(t)
if __name__=="__main__":
    print("=== Basic String Problems ===")
    t="hello";print(f"Reverse: '{t}' -> '{rs(t)}' (slicing), '{rip(t)}' (reversed), '{rtp(t)}' (two-pointer)")
    t="racecar";print(f"Palindrome '{t}': {ip(t)} (iterative), {ips(t)} (slicing), {ipic(t)} (ignore case)")
    t="A man, a plan, a canal: Panama";print(f"Palindrome '{t}': {ipic(t)}")
    t="52";print(f"Largest odd in '{t}': '{lon(t)}'")
    t=["flower","flow","flight"];print(f"LCP of {t}: '{lcp(t)}'")
    t=["dog","racecar","car"];print(f"LCP of {t}: '{lcp(t)}'")
    s,t="egg","add";print(f"Isomorphic '{s}' & '{t}': {iso(s,t)}")
    s,t="foo","bar";print(f"Isomorphic '{s}' & '{t}': {iso(s,t)}")
    s,t="paper","title";print(f"Isomorphic '{s}' & '{t}': {iso(s,t)}")
    s,t="waterbottle","erbottlewat";print(f"Rotation: '{s2}' is rot of '{s1}': {rot(s1,s2)}")
    s,t="hello","world";print(f"Anagrams: '{s}' & '{t}': {ana(s,t)}")
    s,t="anagram","nagaram";print(f"Anagrams: '{s}' & '{t}': {ana(s,t)}")