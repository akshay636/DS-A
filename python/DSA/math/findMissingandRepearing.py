def missingRepeat(arr):
  result = {'missing':-1, 'repeating':-1}
  n=len(arr)
  temp = [0]*n
  for i in range(0,n):
    temp[arr[i]-1]=1
  for j in range(0, n):
    if temp[j]==0:
      result['missing']=j+1
      break
  for i in range(n):
    for j in range(i+1, n):
      if arr[i]==arr[j]:
        result['repeating']=arr[j]
        break
  return result

print(missingRepeat([1,3,3]))

def opt(arr):
  ans={}
  n =len(arr)
  temp = [0]*n
  for i in range(0,n):
    temp[arr[i]-1]+=1
    if temp[arr[i]-1]>1:
      ans['repeating'] = arr[i]
      break
  for i in range(0,n):
    if temp[i]==0:
      ans['missing'] =i+1
      break
  return ans
print(opt([1,3,3]))