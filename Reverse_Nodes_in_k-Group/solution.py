# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def reverse(self, head, k):
        if head== None:
            return None
        if k == 1 :
            return head

        tmp_head = ListNode(-1)
        tmp_head.next = head

        reverse_head = ListNode(-1)
        front, reverse_tail = head, head

        while k > 0:
            if k == 1 :
                last = front.next

            tmp_next = front.next    
            front.next = reverse_head.next
            reverse_head.next = front

            front = tmp_next
            k -= 1

        reverse_tail.next = last

        return reverse_head.next

    def reverseKGroup(self, head, k):
        tmp_head = ListNode(-1)
        tmp_head.next = head

        first, second = tmp_head, tmp_head 

        while True:
            second = first 
            isValid = True
            for i in range(k):
                if second.next == None:
                    isValid = False
                    break
                second = second.next
            if not isValid:
                break 
            else:
                first.next = self.reverse(first.next, k)

            for i in range(k):
                first = first.next
             
        return tmp_head.next 
        

def print_list(head):
    p = head
    while p is not None:
        print p.val, 
        p = p.next
    print ""

def gen_list():
    tmp_head = ListNode(-1)
    tmp_p = tmp_head
    for i in range(10):
        node = ListNode(i)
        tmp_p.next = node
        tmp_p = tmp_p.next

    return tmp_head.next

if __name__ == "__main__":

    head = Solution().reverseKGroup(gen_list(), 1)
    print_list(head)
    print ""

    head = Solution().reverseKGroup(gen_list(), 2)
    print_list(head)
    print ""

    head = Solution().reverseKGroup(gen_list(), 3)
    print_list(head)
    print ""