# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = head
        slow = head
        last = None
        while True:
            if fast is None or fast.next is None:
                return None
            else:
                fast = fast.next.next
                slow = slow.next

                if last is not None:
                    last = last.next

                if fast == slow and last is None:
                    last = head
                if last == slow:
                    return last

        return None
# def gen_list(array_list):

if __name__ == "__main__":
    p0 = ListNode(0)
    p = ListNode(1)
    p2 = ListNode(2)
    p0.next = p 
    p.next = p2
    p2.next = p 
    print Solution().detectCycle(p0).val


