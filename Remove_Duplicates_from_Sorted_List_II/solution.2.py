# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None

        tmp_head = ListNode(head.val - 1)
        tmp_head.next = head 

        slow_p = tmp_head
        while slow_p is not None:
            if slow_p.next is None:
                break 
            if slow_p.next.next is None:
                break
            if slow_p.next.val == slow_p.next.next.val:
                dup_v = slow_p.next.val
                p = slow_p.next
                while p is not None and p.val == dup_v:
                    p = p.next
                slow_p.next = p 
                continue
                
            slow_p = slow_p.next  
        return tmp_head.next 


