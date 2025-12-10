def isPalindrome(string):
    left, right = 0, len(string) -1
    while left < right:
        while left < right and not alphaNum(string[left]):
            left +=1
        while right > left and not alphaNum(string[right]):
            right -=1
        if string[left].lower() != string[right].lower():
            return False
        left, right = left+1, right -1
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

def twoPointer(nums=[1,2,3,4,5,6], target=6):
    result : list[int] = list()
    left, right = 0, len(nums) -1
    while left < right:
        if nums[left] + nums[right] > target and left < right:
            right-=1
        elif nums[left] + nums[right] < target and right > left:
            left+=1
        else:
            result.append((nums[left], nums[right]))
            left,right = left+1, right-1
    return result

print(twoPointer())

