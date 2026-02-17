"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2  
Output: 4  
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1  
Output: 2  
Explanation: The longest substring with no more than '1' distinct characters is "aa".
"""
from collections import Counter
class Solution:
    def findLength(self, str1:str, k:int):
        best_len = 0
        #TODO: Write your code here
        count_iter = 0
        result = list()
        left = 0
        freq_map = Counter()
        if len(str1) <= 1:
            raise ValueError('input string length cannot be empty or 1')
        for right in range(len(str1)):
            freq_map[str1[right]] +=1
            while len(freq_map) > k:
                freq_map[str1[left]] -=1
                if freq_map[str1[left]] == 0:
                    del freq_map[str1[left]]
                left += 1
            best_len = max(best_len, right-left+1)
        return best_len, result
sol = Solution()
print(sol.findLength('araaci', 2))

"""
Thoughts for this problem:
start from the left of the string
expand window by one:
check to see if the num of distinct chars is greater than k:
if yes:
    shrink the window from the left by removing leftmost char from curr_window
    if the leftmost char doesn't show up in freq_map then we remove it
    move left by one
update the window since it is valid now
return best_len
"""