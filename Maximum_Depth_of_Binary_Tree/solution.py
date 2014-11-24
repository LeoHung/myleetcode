# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer

    def maxDepth(self, root):
        self.max = 0
        self.traverse(root, 1)

        return self.max

    def traverse(self, node, depth):
        if node == None:
            return

        if depth > self.max :
            self.max = depth

        self.traverse(node.left, depth +1)
        self.traverse(node.right, depth +1)

