# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        tmp_head = ListNode(-1)
        tmp_head.next = ListNode(-1)
        tmp_head.next.next = head 
        firstP, secondP = tmp_head, tmp_head

        for i in range(m):
            firstP = firstP.next
        for i in range(n):
            secondP = secondP.next
        secondP = secondP.next.next

        reverseP = ListNode(-1)

        d_firstP = firstP.next
        last_one = d_firstP

        for i in range(n-m+1):
            tmp = reverseP.next
            reverseP.next = d_firstP
            d_firstP = d_firstP.next
            reverseP.next.next = tmp 

        firstP.next = reverseP.next
        last_one.next = secondP

        return tmp_head.next.next

if __name__ == "__main__":
    x = ListNode(5)
    print Solution().reverseBetween(x ,1 ,1).val

