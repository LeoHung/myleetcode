# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head

        tmp_head = ListNode(-1)
        tmp_head.next = head

        last = tmp_head

        while last != None:
            first = last.next
            if first == None:
                break
            second = first.next
            if second == None:
                break

            first.next, second.next = second.next, first
            last.next = second

            if last.next == None or last.next.next == None:
                break
            last = last.next.next

        return tmp_head.next
