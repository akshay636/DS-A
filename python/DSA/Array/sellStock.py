def maxProfit(prices):
  if not prices:
    return 0
  min = prices[0]
  max_p = 0 
  for i in prices:
    if min>i:
      min=i
    else:
      max_p= max(max_p, i-min)
  return max_p

print(maxProfit([7,1,5,3,6,4]))