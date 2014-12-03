# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        return self.sort(head)

    # return sorted head and tail
    def sort(self, head):
        if head == None or head.next == None:
            return head

        # split into two parts
        slow_p = head
        fast_p = head

        while fast_p.next and fast_p.next.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # split
        left_head = head
        right_head = slow_p.next
        slow_p.next = None

        sorted_left_head = self.sort(left_head)
        sorted_right_head = self.sort(right_head)

        # merge
        return self.merge(sorted_left_head, sorted_right_head)

    def merge(self, sorted_left_head, sorted_right_head):
        new_head = ListNode(0)
        new_tail = new_head

        while sorted_left_head and sorted_right_head:
            if sorted_left_head.val < sorted_right_head.val:
                new_tail.next = sorted_left_head
                new_tail = new_tail.next
                sorted_left_head = sorted_left_head.next
            else:
                new_tail.next = sorted_right_head
                new_tail = new_tail.next
                sorted_right_head = sorted_right_head.next

        if not sorted_left_head == None:
            new_tail.next = sorted_left_head
        if not sorted_right_head == None:
            new_tail.next = sorted_right_head

        return new_head.next
