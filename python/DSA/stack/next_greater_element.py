# def next_greater_el(nums1,nums2):
#   stack =[]
#   for i in nums1:
#     cur = -1
#     for j in nums2:
#       if i<j and nums2.index(i)!=len(nums2)-1:
#         cur = j
#         break
#       else:
#         cur = -1
#     stack.append(cur)
#   return stack
  
# print(next_greater_el([1,3,5,2,4],[5,4,3,2,1]))

def next_greater_el(nums1,nums2):
  stack =[]
  for i in nums1:
    cur = -1
    for j in range(nums2.index(i),len(nums2)):
      if i<nums2[j] and nums2.index(i)!=len(nums2)-1:
        cur = nums2[j]
        break
      else:
        cur = -1
    stack.append(cur)
  return stack
  
print(next_greater_el([2,4],[1,2,3,4]))
