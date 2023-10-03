def index(arr, target, i, curSum, temp):
  ans = []
  if curSum>target:
    return ans
  
  if i == len(arr):
    if curSum ==target:
      ans.append(temp[:])
    return ans
  curSum+= arr[i]
  temp.append(arr[i])
  ans+= index(arr, target,i,curSum, temp)
  curSum-=arr[i]
  temp.pop()
  ans+= index(arr, target, i+1, curSum, temp)
  return ans

arr = [2, 3, 6, 7]
target = 7
ans = index(arr, target, 0, 0, [])
print(ans)


# optimize
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, curSum, temp):
            if curSum == target:
                ans.append(temp[:])
                return
            if curSum > target or index == len(candidates):
                return
            
            for i in range(index, len(candidates)):
                curNum = candidates[i]
                temp.append(curNum)
                backtrack(i, curSum + curNum, temp)
                temp.pop()
        
        ans = []
        backtrack(0, 0, [])
        return ans

            