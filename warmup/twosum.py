class Solution:
    def twoSum(self,nums:list, target:int, answer:set) -> int:
        """Find two numbers in the array that sum up to the target
        EX: [2,7,11,15]
        target = 9
        """
        #TODO: Write your code here
        hash_map = dict()
        for i, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = i
        for i, num in enumerate(nums):
            desired_num = target - num
            if desired_num in hash_map and hash_map[desired_num] != i:
                return(i,hash_map[desired_num])
        
solution = Solution()

res = solution.twoSum(nums= [2,7,11,15], target=9, answer=(0,1))

print(f'result: {res}, expected: (0,1)')