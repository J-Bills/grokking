class Node:
    def __init__(self, value, next=None):
    self.val = value
    self.next = next

class Solution:
    def isPalindrome(self, head):
        # TODO: Write your code here
        if not head or not head.next:
            return True
        fast, slow = head, head
        #incrementing like this to get slow to be at the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #setting up the comparison for the first half of the list with the second half
        first_half = head
        second_half = self.reverseList(slow)
        #checking if the second half of the list matches the first
        while second_half:
            if second_half.val != first_half.val:
                return False
        first_half = first_half.next
        second_half = second_half.next
        return True

    #helper function that takes the second half of the list and reverses it using pointers
    #check: Reversing a Linked List
    def reverseList(self, head):
        prev, slow = None, head
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        return prev
def main():
    sol = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(sol.isPalindrome(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(sol.isPalindrome(head)))

main()