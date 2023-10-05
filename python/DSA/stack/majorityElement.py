import math
def majorityElement1(nums):
  n = len(nums)//3
  print(n)
  till = len(nums)
  count ={}
  newAr =[]
  for i in nums:
    if i in count:
      count[i] =count[i]+1
    else:
      count[i] =1
  for key, value in count.items():
    if value>n:
      newAr.append(key)
  return newAr

print(majorityElement1([1,2,3,5]))
def majorityElement(nums):
    if not nums:
        return []

    count1, count2, candidate1, candidate2 = 0, 0, None, None

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    n = len(nums)
    result = []

    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Example usage:
# nums1 = [3, 2, 3]
# print(majorityElement(nums1))  # Output: [3]

# nums2 = [1]
# print(majorityElement(nums2))  # Output: [1]

# nums3 = [1,3, 2]
# print(majorityElement(nums3))  # Output: [1, 2]
