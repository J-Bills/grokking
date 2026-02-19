"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Note: Positive numbers start from '1'.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
"""

class Solution:
    def findNumber(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            # include the checks for the the number being in the bounds of the list
            # and bigger than 0 with the check for if swapping needs to happen
            # so that we can skip those cases.
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]: 
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
            for i in range(len(nums)):
                if nums[i] != i+1:
                    return i+1
sol = Solution()
print(sol.findNumber([3, -2, 0, 1, 2]))