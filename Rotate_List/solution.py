# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def get_len(self, head):
        p = head
        count = 0
        while(not p == None):
            count +=1
            p = p.next
        return count

    def get_last(self, head):
        p = head
        if p == None:
            return None

        while(not p.next == None):
            p = p.next
        return p

    def rotateRight(self, head, k):
        # count n
        n = self.get_len(head)
        if n <= 1:
            return head

        k = k % n
        if k == 0:
            return head
        if n == k:
            return head


        i = n - k - 1
        p = head
        while i > 0:
            p = p.next
            i -= 1

        new_head = p.next
        # cut
        p.next = None

        tail = self.get_last(new_head)
        if not tail == None:
            tail.next = head
        return new_head


