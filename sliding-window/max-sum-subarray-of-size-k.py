""" Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

Example 1:

Input: arr = [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: arr = [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""

class Solution:
    def findMaxSumSubArray(self,k, arr):
        # TODO: Write your code here
        result = list()
        max_sum = 0
        window_sum = 0
        
        #summing the values up to k starting from 0
        window_sum = sum(arr[:k])
        #initializing the beginning max sum to that window_sum for comparison later
        max_sum = window_sum
        
        # we want to slide the window the right by one space and calculate the sum of that slice
        # after sliding forward we want to remove the last element from our sum
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum
    
    def findMaxSumSubArray2(self, k, arr):
        #TODO: Find the max sum subarray but include the indecies that resulted in the max sum

        #same thing as before but we have a pointer to the beginning of the array that becomes the max_sum
        if k<= 0 or k>len(arr):
            raise ValueError("k must be between 1 and len(nums)")
        result = list()
        best_start = 0
        
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            
            start = i-k+1
            if window_sum > max_sum:
                max_sum = window_sum
                best_start = start
        result = arr[best_start:best_start+k]
        return result
sol = Solution()
# print(sol.findMaxSumSubArray(k=2, arr=[2,3,4,1,5]))
print(sol.findMaxSumSubArray2(k=3, arr=[2,3,4,1,5]))
