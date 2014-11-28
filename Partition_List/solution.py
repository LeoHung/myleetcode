
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        origin_head = head

        first_h = None
        first_t = None
        second_h = None
        second_t = None

        p = head

        while(not p == None):
            if p.val < x:
                if first_h == None :
                    first_h = p
                    first_t = p
                else:
                    first_t.next = p
                    first_t = p
            else:
                if second_h == None:
                    second_h = p
                    second_t = p
                else:
                    second_t.next = p
                    second_t = p

            p = p.next

        if not first_t == None:
            first_t.next = None

        if not second_t == None:
            second_t.next = None

        if not first_h == None:
            first_t.next = second_h
            return first_h
        else:
            return second_h

