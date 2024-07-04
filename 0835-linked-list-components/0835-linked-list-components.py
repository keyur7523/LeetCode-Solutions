# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        d = []
        curr = head
        while curr:
            if curr.val in nums:
                d.append([curr.val])
                break
            curr = curr.next
        while curr.next is not None:
            flag = 0
            if curr.next.val in nums:
                for i in d:
                    if curr.val in i:
                        i.append(curr.next.val)
                        flag = 1
                if not flag:
                    d.append([curr.next.val])
            curr = curr.next
       
        return len(d)

                    
            
                
        