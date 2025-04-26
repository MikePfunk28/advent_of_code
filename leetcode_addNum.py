from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current: Optional[ListNode] = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get the values one at a time and add them.
            # List Comprehension, basically if l1:, return the first value,
            # if there is a value return it otherwise return no value or 0.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # New value
            # This is almost counter-intuitive, as we are adding the numbers digit by digit.
            # The carry is going to have the remainder cut off from rounding using int types.
            # So we use modulo to get the remainder to know what the digit is to add.
            # calculate the value or the sum to store in the new LinkedList
            val = val1 + val2 + carry
            # calculate the carry separately.
            carry = val // 10
            # Get modulo or remainder
            val = val % 10
            # If val1 + val2 + carry >= 10:
            #    return carry = 1

            current.next = ListNode(val)

    
            # Update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    # This is how you would reverse the value, but is not needed.
    # The numbers are already aligned how you would add them.
    # E.g. 342 + 465 is 807, so instead of having to add the last
    # digit first, we can just add in order.  
    
    # So essentially if we remember the previous node, we can
    # just have the next node be previous, and tail be head.
    def print_reversed(self, head) -> None:
        """Print the linked list in reverse order."""
        if head is None:
            return
        self.print_reversed(head.next)
        print(head.val, end=" ")

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution().addTwoNumbers(l1, l2)
# This while loops is not needed, but if you had multiple answers, 
# you could use it.
#while result:
    #print(result.val, end=" ")
    #result = result.next