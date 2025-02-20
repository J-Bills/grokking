import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    # TODO: Write your code here
    arr.sort()
    n = len(arr)
    smallest_differnce = math.inf
    for i in range(n-2):
      left, right = i+1, n-1
      while left < right:
        target_diff = target_sum - arr[i] - arr[left] - arr[right]
        if target_diff == 0:
          return target_diff
        if abs(target_sum) < abs(smallest_differnce):
          smallest_differnce = target_diff
        
        if target_diff > 0:
          left+=1
        else:
          right-=1
        
    return target_sum - smallest_differnce

sol = Solution()
sol.searchTriplet(arr=[0,0,1,1,2,6], target_sum=5)
