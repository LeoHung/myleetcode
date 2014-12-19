# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pA, pB = headA, headB

        if pA == None or pB == None:
            return None

        A_count = 0 
        B_count = 0
        while not(pA.next == None or pB.next == None):
            pA = pA.next
            pB = pB.next
            A_count += 1 
            B_count += 1 

        last = None
        if pA.next == None:
            last = pA
            while pB.next is not None:
                pB = pB.next
                B_count += 1
        elif pB.next == None:
            last = pB
            while pA.next is not None:
                pA = pA.next
                A_count += 1 

        if pA != pB:
            return None
        else: 
            pA, pB = headA, headB
            if A_count > B_count:
                delta = A_count - B_count
                while delta > 0:
                    pA = pA.next
                    delta -= 1 
            elif B_count > A_count:
                delta = B_count - A_count
                while delta > 0:
                    pB = pB.next
                    delta -= 1 

            while not(pA is None or pB is None):
                if pA == pB:
                    return pA
                pA = pA.next
                pB = pB.next
            return None
            

if __name__ == "__main__":
    print Solution().getIntersectionNode(ListNode(-1), ListNode(-1))
    a = ListNode(-1)
    b = ListNode(-2)
    c = ListNode(-3)
    d = ListNode(-4)
    e = ListNode(-5)
    a.next = c
    b.next = d 
    d.next = c
    c.next = e
    print Solution().getIntersectionNode(a, b).val

    print Solution().getIntersectionNode(a, a).val