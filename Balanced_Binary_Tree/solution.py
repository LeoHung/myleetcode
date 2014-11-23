# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isBalanced(self, root):
        if root == None:
            return True

        self.is_b =  True
        self.get_depth(root, 0)

        return self.is_b

    def get_depth(self, node, depth):
        if(node == None or self.is_b == False):
            return depth

        left_depth = self.get_depth(node.left, depth +1)
        right_depth = self.get_depth(node.right, depth +1)

        if abs(left_depth - right_depth ) > 1:
            self.is_b = False

        return max([left_depth, right_depth])




