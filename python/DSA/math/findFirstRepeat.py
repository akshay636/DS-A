def findFirstRepeating(arr):
  for i in range(0, len(arr)):
    for j in range(i+1,len(arr)):
      print(arr[i],arr[j])
      if(arr[i]==arr[j]):
        return arr[i]
  return -1

arr =[6, 10, 5, 4, 9, 1,120, 4, 1, 10]
print(findFirstRepeating(arr))
# Time Complexity: O(N2)
# Auxiliary Space: O(1)

