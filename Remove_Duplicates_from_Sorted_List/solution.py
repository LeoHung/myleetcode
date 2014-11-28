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

        prev = head
        cur = head.next

        while True:
            if cur == None:
                break
            if prev.val == cur.val:
                cur = cur.next
                prev.next = cur
                continue
            else:
                prev, cur = cur, cur.next

        return head


