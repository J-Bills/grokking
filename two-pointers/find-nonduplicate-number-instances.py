
class Solution:
    def moveElements(self, arr):
        """
        Given an array of sorted numbers, move all non-duplicate number instances at the 
        beginning of the array in-place. 
        The non-duplicate numbers should be sorted and you should not use any extra space 
        so that the solution has constant space complexity i.e., O(1) .

        Move all the unique number instances at the beginning of the array and 
        after moving return the length of the subarray that has no duplicate in it.
        """
        # TODO: Write your code here
        fp = 1
        next_non_duplicate = 1
        while(fp <len(arr)):
            if arr[fp] != arr[next_non_duplicate-1]:
                arr[next_non_duplicate] = arr[fp]
                next_non_duplicate+=1
            fp+=1
        print(arr)
        return next_non_duplicate
    
    
sol = Solution()
arr = [2, 3, 3, 3, 6, 9, 9]
result = sol.moveElements(arr)
print(f'result: {result}')

def binarySeach(arr, target):
    l,r = 0, len(arr) -1
    while l<=r:
        m = l+r//2
        if arr[m]<target:
            l = m +1
        elif arr[m]>target:
            r = m-1
        else:
            return m
    return -1