""" Fruits into Baskets
    You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

    You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

    Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
    You can start with any tree, but you can’t skip a tree once you have started.
    You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both baskets.

    Example 1:

    Input: arr=['A', 'B', 'C', 'A', 'C']  
    Output: 3  
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
    
"""
from collections import Counter
class Solution():
    def find_length(self, arr:list):
        """
        Thoughts for this problem:
        start at the left of the lits
        set max_len = 0
        set freq_map = Counter()
        for every tree in the farm we add the tree to our map:
            add that tree to our basket
            while there are more than 2 different trees in our basket remove the left leftmost one, if that value is equal to zero then remove it from basket
            increment left at the end of the step
            compare max_len to total fruits in our basket
            return max_len
        """
        max_length = 0
        left = 0
        baskets = Counter()
        for right in range(len(arr)):
            baskets[arr[right]] += 1
            while len(baskets) > 2:
                baskets[arr[left]] -=1
                if baskets[arr[left]] == 0:
                    del baskets[arr[left]]
                left +=1
            max_length = max(max_length, right-left+1)
        return max_length
    

sol = Solution()
# print(sol.find_length(['A','B','C','A','C']))
print(sol.find_length(["A", "A", "A", "A", "B", "B", "B", "C", "C", "C"]))