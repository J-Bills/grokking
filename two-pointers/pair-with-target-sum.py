
class Solution:
    def search(self, arr, target_sum):
        """Given an array of numbers sorted in ascending order and a target sum,
        find a pair in the array whose sum is equal to the given target.

        Write a function to return the indices of the two numbers (i.e. the pair) 
        such that they add up to the given target. If no such pair exists return [-1, -1]."""
        # TODO: Write your code here
        fp, lp = 0, len(arr) -1
        while fp < lp:
            if arr[lp] + arr[fp] > target_sum:
                lp -= 1
            elif arr[lp] + arr[fp] < target_sum:
                fp += 1
            else:
                return [fp,lp]
        return [-1, -1]
    
sol = Solution()
arr = [1, 2, 3, 4, 6]
target_sum = 6
result = sol.search(arr, target_sum)
print(f"result: {result}, expected output: {6}")