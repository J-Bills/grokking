class Solution:
    def find(self, num):
    # TODO: Write your code here
        fast, slow = num, num
        while True:
            #doing the calc for fast twice
            fast = self.calc(self.calc(fast))
            slow = self.calc(slow)
            if fast == slow:
                break
        if slow == 1:
            return True
        return False

    def calc(self, num):
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10 
        return _sum
    
def main():
    sol = Solution()
    print(sol.find(23))
    print(sol.find(155))
    
main()