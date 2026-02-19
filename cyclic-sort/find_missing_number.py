"""
Find the missing number
We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
"""

class Solution:
    def findMissingNumber(self, nums:int):
        n = len(nums)
        i = 0
        while i<n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
                
        for i in range(n):
            if nums[i] != i:
                return i
            
        return 0
    
    
sol = Solution()
print(sol.findMissingNumber([8, 3, 5, 2, 4, 6, 0, 1]))