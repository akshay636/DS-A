# Given an array arr[] of size N-1 with integers in the range of [1, N],
# the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.
# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
# Output: 5
# Explanation: The missing number between 1 to 8 is 5

# Find Missing Element

arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)
def findMissing(arr,n):
  temp =[0]*(n+1)
  for i in range(0,n):
    temp[arr[i]-1] =1
  print(temp)
  for j in range(0, n+1):
    if temp[j]==0:
      ans =j+1
  return ans
print(findMissing(arr,n))

def opt(nums):
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum
print(opt([1, 2, 4, 6, 3, 7, 8]))