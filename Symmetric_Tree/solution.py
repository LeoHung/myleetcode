class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorder(self, l, node, isLeft):
        if node == None:
            return
        l.append(node.val)
        if isLeft:
            self.preorder(l, node.left, isLeft)
            self.preorder(l, node.right, isLeft)
        else:
            self.preorder(l, node.right, isLeft)
            self.preorder(l, node.left, isLeft)
    def inorder(self, l, node, isLeft):
        if node == None:
            return
        if isLeft:
            self.inorder(l, node.left, isLeft)
            l.append(node.val)
            self.inorder(l, node.right, isLeft)
        else:
            self.inorder(l, node.right, isLeft)
            l.append(node.val)
            self.inorder(l, node.left, isLeft)

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        left_first_preorder = list()
        self.preorder(left_first_preorder, root, True)
        right_first_preorder = list()
        self.preorder(right_first_preorder, root, False)

        if not left_first_preorder == right_first_preorder:
            return False


        left_first_inorder = list()
        self.inorder(left_first_inorder, root, True)
        right_first_inorder = list()
        self.inorder(right_first_inorder, root, False)

        if not left_first_inorder == right_first_inorder:
            return False

        return True

if __name__ == "__main__":
    head_t = TreeNode(1)
    n_1 = TreeNode(2)
    n_2 = TreeNode(2)
    head_t.left = n_1
    head_t.right = n_2

    n_3 = TreeNode(3)
    n_4 = TreeNode(3)
    n_1.right = n_3
    n_2.right = n_4

    print Solution().isSymmetric(head_t)

