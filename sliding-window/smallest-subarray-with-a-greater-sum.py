"""
Docstring for smallest-subarray-with-a-greater-sum
Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Example 1:

Input: arr = [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: arr = [2, 1, 5, 2, 8], S=7
Output: 1 
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

"""

class Solution:
    def smallest_subarray(self, arr, s):
        #TODO: Write the code here
        window_sum = 0
        min_len = float('inf')
        left = 0
        result_list = list()
        
        for right in range(len(arr)):
            window_sum+=arr[right]
            while window_sum >=s:
                min_len = min(min_len, right-left+1)
                array = arr[left:right+1]
                result_list.append(array)
                window_sum-=arr[left]
                left+=1
            
        for array in result_list:
            if len(array) > min_len:
                result_list.remove(array)
        return min_len, result_list
    
sol = Solution()
print(sol.smallest_subarray([2, 1, 5, 2, 3, 2], 7))