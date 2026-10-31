# How to implement binary search?
def bs(a,t):
 l,r=0,len(a)-1
 while l<=r:
  m=(l+r)//2
  if a[m]==t:return m
  l,r=(m+1,r)if a[m]<t else(l,m-1)
 return -1
def bs_rec(a,t,l=0,r=None):
 if r is None:r=len(a)-1
 if l>r:return -1
 m=(l+r)//2
 return m if a[m]==t else bs_rec(a,t,m+1,r)if a[m]<t else bs_rec(a,t,l,m-1)
def bs_left(a,t):
 l,r=0,len(a)-1;res=-1
 while l<=r:
  m=(l+r)//2
  if a[m]==t:res=m;r=m-1
  elif a[m]<t:l=m+1
  else:r=m-1
 return res
def bs_right(a,t):
 l,r=0,len(a)-1;res=-1
 while l<=r:
  m=(l+r)//2
  if a[m]==t:res=m;l=m+1
  elif a[m]<t:l=m+1
  else:r=m-1
 return res
def bs_count(a,t):
 l=bs_left(a,t)
 return 0 if l==-1 else bs_right(a,t)-l+1