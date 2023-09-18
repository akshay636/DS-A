def twoSum(arr, target):
  obj={}
  for i in range(0, len(arr)):
    comp = target - arr[i]
    if obj.get(comp) is not None:
      return [obj[comp],i]
    else:
      obj[arr[i]] =i
  return []

print(twoSum([3,2,4],6))