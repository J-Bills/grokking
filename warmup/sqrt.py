import math

class Solution:
    def mySqrt(self, x: int) -> int:
        """Compute the sqrt of a given number and return the floor of the result without using built-in functions"""
        # TODO: Write your code here
    
        if x < 2:
            return x
        
        left, right = 2, x//2
        mid = 0
        num = 0
        while left <= right:
            mid =  left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        return right
        
sol = Solution()
result = sol.mySqrt(16)

print(f'result: {result}, expected:{4}')
