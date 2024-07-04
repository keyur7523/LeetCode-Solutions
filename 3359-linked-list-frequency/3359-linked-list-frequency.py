# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        curr = head
        while curr.next:
            if curr.val in d.keys():
                d[curr.val] += 1
            else:
                d[curr.val] = 1
            curr = curr.next
        
        if curr.val in d.keys():
            d[curr.val] += 1
        else:
            d[curr.val] = 1

        curr2 = None

        for i in d.values():
            curr2 = ListNode(i, curr2)
            head2 = curr2

        return curr2

            
        