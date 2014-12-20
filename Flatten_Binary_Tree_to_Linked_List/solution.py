# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root != None:
            self.do(root)

    def do(self, root):
        left, right = None, None
        if root.left is not None:
            left = self.do(root.left)

        if root.right is not None:
            right = self.do(root.right)

        if root.left is not None:
            left_right = left 
            while left_right.right is not None:
                left_right = left_right.right

            left_right.right = right 
            root.right = root.left 
            root.left = None

        return root

def print_tree(root):
    print root.val
    if root.left is not None:
        print "l:"
        print_tree(root.left)
    if root.right is not None:
        print "r:"
        print_tree(root.right)
if __name__ == "__main__":
    root = TreeNode(1)
    v2 = TreeNode(2)
    v3 = TreeNode(3)
    root.left = v2
    v2.left = v3

    Solution().flatten(root)
    print_tree(root)