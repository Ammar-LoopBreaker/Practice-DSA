# How to implement string matching algorithms?
def rk(t,p):
    if not p or not t or len(p)>len(t):return[]
    d,q=256,101;m,n=len(p),len(t);p_hash=t_hash=0;h=1
    for i in range(m-1):h=(h*d)%q
    for i in range(m):p_hash=(d*p_hash+ord(p[i]))%q;t_hash=(d*t_hash+ord(t[i]))%q
    res=[]
    for i in range(n-m+1):
        if p_hash==t_hash:
            if t[i:i+m]==p:res.append(i)
        if i<n-m:t_hash=(d*(t_hash-ord(t[i])*h)+ord(t[i+m]))%q;t_hash=t_hash+q if t_hash<0 else t_hash
    return res
rk_f=lambda t,p:rk(t,p)[0] if rk(t,p)else-1
def bl(p):
    m=len(p);l=[0]*m;le=0;i=1
    while i<m:
        if p[i]==p[le]:le+=1;l[i]=le;i+=1
        else:le=l[le-1] if le else 0;l[i]=le;i+=1
    return l
def kmp(t,p):
    if not p or not t or len(p)>len(t):return[]
    m,n=len(p),len(t);l=bl(p);res=[];i=j=0
    while i<n:
        if p[j]==t[i]:i+=1;j+=1
        if j==m:res.append(i-j);j=l[j-1]
        elif i<n and p[j]!=t[i]:j=l[j-1] if j else 0;i+=1 if not j else 0
    return res
kmp_f=lambda t,p:kmp(t,p)[0] if kmp(t,p)else-1
def z_arr(s):
    n=len(s)
    if n==0:return[]
    z=[0]*n;l=r=0
    for i in range(1,n):
        if i>r:l=r=i
        while r<n and s[r-l]==s[r]:r+=1
        z[i]=r-l;r-=1
    return z
def zfs(t,p):
    if not p or not t or len(p)>len(t):return[]
    c=p+"$"+t;l=len(p);z=z_arr(c)
    return [i-l-1 for i in range(l+1,len(z)) if z[i]==l]
def zf(s):
    if not s:return[]
    n=len(s);z=[0]*n;l=r=0
    for i in range(1,n):
        if i>r:l=r=i
        while r<n and s[r-l]==s[r]:r+=1
        z[i]=r-l;r-=1
    return z
if __name__=="__main__":
    print("=== String Matching Algorithms ===");t=[("ababcabcabababd","ababd"),("aaaaa","bba"),("hello world","world"),("aaaaab","aaa"),("abcde","xyz"),("","a"),("a",""),("mississippi","issip")]
    print("Rabin-Karp Algorithm:");[print(f"  Text: '{txt}', Pattern: '{pat}'\n    All matches: {rk(txt,pat)}\n    First match: {rk_f(txt,pat)}") for txt,pat in t]
    print()
    print("Knuth-Morris-Pratt (KMP) Algorithm:");[print(f"  Text: '{txt}', Pattern: '{pat}'\n    All matches: {kmp(txt,pat)}\n    First match: {kmp_f(txt,pat)}") for txt,pat in t]
    print()
    print("Z-function Search:");[print(f"  Text: '{txt}', Pattern: '{pat}'\n    Matches: {zfs(txt,pat)}") for txt,pat in t]
    print()
    print("Z-function Computation:");[print(f"  '{s}' -> Z = {zf(s)}") for s in ["aabcaabxaaaz","aaaaaa","abababab","abcdef"]]