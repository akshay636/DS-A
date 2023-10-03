def singleNumber(nums):
  most_f =None
  max_c =0
  count={}
  for num in nums:
    if count.get(num):
      count[num] = count[num] + 1
    else:
      count[num] = 1
    if count[num] > max_c:
      max_c =count[num]
      most_f = num
  return most_f
    

print(singleNumber([3,2,3]))
