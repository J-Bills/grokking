
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def findCycleStart(self, head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            # break if the two pointers meet
            if fast == slow:
                break
        else:
            return None
        #set slow to head and increment through both pointers until they meet to find the cycle point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    

def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Create a cycle by connecting nodes
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

    # Create a different cycle
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

    # Create a cycle that points back to the head
    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

main()