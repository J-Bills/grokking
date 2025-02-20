class Solution:
  def searchTriplets(self, arr):
    triplets = []
    # TODO: Write your code here
    arr.sort()
    count = 0
    n = len(arr)
    for i in range(n-2):
      if i>0 and arr[i] == arr[i-1]:
        continue

      left, right = i+1, n-1

      while(left < right):
        cursum = arr[left] + arr[right] + arr[i]
        if cursum == 0:
          triplets.append([arr[i], arr[left], arr[right]])
          left +=1
          right -=1

          while left<right and arr[left] == arr[left-1]:
            left+=1
          while left<right and arr[right] == arr[right+1]:
            right-=1
        elif cursum < 0:
          left+=1
        else:
          right-=1


    return triplets

sol = Solution()
data = [-3,0,1,2,-1,1,-2]
result = sol.searchTriplets(data)
print(result)
