"""
We are given an unsorted array containing n+1 numbers taken from the range 1 to n.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space.
You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
"""

class Solution:
    def find_the_duplicate_number(self, arr):
        i= 0
        while i < len(arr):
            j = arr[i] -1
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else: 
                i+=1
        for i in range(len(arr)):
            if arr[i] != i+1:
                return arr[i]
        return arr
    
    
sol = Solution()
print(sol.find_the_duplicate_number([2, 1, 3, 3, 5, 4]))