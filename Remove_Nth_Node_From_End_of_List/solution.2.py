# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        tmp_head = ListNode(-1)
        tmp_head.next = head
        right_p = tmp_head
        left_p = None

        while right_p.next is not None:
            if left_p is not None:
                left_p = left_p.next

            n -= 1
            if n == 0:
                left_p = tmp_head

            right_p = right_p.next

        if left_p is not None:
            left_p.next = left_p.next.next

        return tmp_head.next

if __name__ == "__main__":
    n = ListNode(1)
    print Solution().removeNthFromEnd(n, 1)