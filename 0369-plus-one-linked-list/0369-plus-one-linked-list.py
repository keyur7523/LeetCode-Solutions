# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

# 1 -> 2 -> 3 -> 4

        curr = head
        s = ''
        while curr.next is not None:
            s += str(curr.val)
            curr = curr.next
        s += str(curr.val)
        p = int(s)
        p += 1

        head2 = None
        current = head2

        for i in str(p):
            if head2 is None:
                head2 = ListNode(i, None)
            else:
                current = head2
                while current.next is not None:
                    current = current.next 
                current.next = ListNode(i, None)

        return head2
        
        