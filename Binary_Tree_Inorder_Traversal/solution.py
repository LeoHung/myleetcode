# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def travel(self, l, node):
        if node == None:
            return 
        self.travel(l, node.left)
        l.append(node.val)
        self.travel(l, node.right)
        
    def inorderTraversal(self, root):
        l = []
        self.travel(l, root)
        return l
