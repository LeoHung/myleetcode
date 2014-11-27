# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def check(self, node, min_v, max_v):
        if node == None:
            return True

        if not min_v == None and  node.val <= min_v:
            return False

        if not max_v == None and node.val >= max_v:
            return False

        return self.check(node.left, min_v, node.val) and self.check(node.right, node.val, max_v)

    def isValidBST(self, root):
        return self.check(root, None, None)
