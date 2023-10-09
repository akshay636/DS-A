def good_pair(ar):
  if not ar:
    return 0
  count =0
  for i in range(0,len(ar)):
    for j in range(0,len(ar)):
      if ar[i]==ar[j] and i<j:
        count += 1
  return count

print(good_pair([1,2,3,1]))