ar =[0,0,1,1,1,1,2,3,3]
# def dupl_arr_2(nums):
#   if not nums:
#     return 0
#   count =1
#   i=1
#   while i<len(nums):
#     if nums[i] == nums[i-1]:
#       count += 1
#       if count>2:
#         nums.pop(i)

#       else:
#         i += 1
#     else:
#       count =1
#       i += 1
#   return len(nums)

# print(dupl_arr_2(ar))
      

def removeDuplicates(nums):
  count={}
  for i in nums:
    if count.get(i):
      count[i] = count[i]+1
      if count[i]>2:
        print(i)
        nums.pop(i)
    else:
      count[i] = 1
  return count

print(removeDuplicates(ar))
print(ar)