def mySqrt(x):
  if x==0 or x==1:
    return 0
  j,k=1,x
  while(j<=k):
    mid = j + (k- j) //2
    print(j,k,mid)
    sq = mid * mid
    if sq ==x:
      return mid
    elif sq<x:
      j=mid+1
    else:
      k =mid-1
  return k
print(mySqrt(5))