# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrderBottom(self, root):
        self.depth2nodes = {}

        self.traverse(root, 0)

        out = []
        for depth in sorted(self.depth2nodes, reverse=True):
            out.append(self.depth2nodes[depth])

        return out

    def traverse(self, node, depth):
        if node == None:
            return

        self.traverse(node.left, depth +1)

        if not self.depth2nodes.has_key(depth):
            self.depth2nodes[depth] = []
        self.depth2nodes[depth].append(node.val)

        self.traverse(node.right, depth +1)
