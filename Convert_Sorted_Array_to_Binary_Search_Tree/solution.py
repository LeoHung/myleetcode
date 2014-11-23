# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num == None or len(num) == 0:
            return None


        length = len(num)
        mid = length/2

        left = self.getBST(num, 0, mid-1)
        midNode = TreeNode(num[mid])
        right = self.getBST(num, mid+1, length-1)

        midNode.left = left
        midNode.right = right

        return midNode

    def getBST(self, num, start, end):
        if end < start :
            return None

        mid = (start + end)/2

        left = self.getBST(start, mid-1)

        tn = TreeNode(num[mid])

        right = self.getBST(mid+1, end)

        tn.left = left
        tn.right = right

        return tn
