# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLength(self, head):
        p = head
        l = 0
        while(p != None):
            l +=1
            p = p.next
        return l

    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None

        l = self.getLength(head)

        mid = l/2

        self.h = head

        left = self.getBST(0, mid-1)
        midNode = TreeNode(self.h.val)
        self.h = self.h.next
        right = self.getBST(mid+1, l-1)
        midNode.left = left
        midNode.right = right

        return midNode


    def getBST(self, start, end):
        if(end < start):
            return None

        mid = (start + end)/2

        left = self.getBST(start, mid-1)
        midNode = TreeNode(self.h.val)
        self.h = self.h.next
        right = self.getBST(mid+1, end)

        midNode.left = left
        midNode.right = right

        return midNode

def printTree(node):
    if node == None:
        return
    printTree(node.left)
    print node.val
    printTree(node.right)


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    s = Solution()
    printTree( s.sortedListToBST(n1) )
