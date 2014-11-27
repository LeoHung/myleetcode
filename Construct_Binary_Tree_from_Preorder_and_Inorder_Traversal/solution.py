# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param preorder, a list of integers
    # @return a tree node
    # right is not included
    def toBuildTree(self, inorder_left_i, inorder_right_i, preorder_left_i, preorder_right_i):

        if(inorder_right_i <= inorder_left_i or preorder_right_i <= preorder_left_i):
            return None

        midNodeValue = self.preorder[preorder_left_i]
        midNode = TreeNode(midNodeValue)

        inorder_mid_i = -1

        for i in range(inorder_left_i, inorder_right_i):
            if self.inorder[i] == midNodeValue:
                inorder_mid_i = i

        preorder_mid_i = preorder_left_i + 1 + (inorder_mid_i - inorder_left_i)

        new_inorder_left_left_i = inorder_left_i
        new_inorder_left_right_i = inorder_mid_i
        new_preorder_left_left_i = preorder_left_i + 1
        new_preorder_left_right_i = preorder_mid_i

        leftNode = self.toBuildTree(
                        new_inorder_left_left_i,
                        new_inorder_left_right_i,
                        new_preorder_left_left_i,
                        new_preorder_left_right_i)

        new_inorder_right_left_i = inorder_mid_i+1
        new_inorder_right_right_i = inorder_right_i
        new_preorder_right_left_i = new_preorder_left_right_i
        new_preorder_right_right_i = preorder_right_i

        rightNode = self.toBuildTree(
                        new_inorder_right_left_i,
                        new_inorder_right_right_i,
                        new_preorder_right_left_i,
                        new_preorder_right_right_i
                    )

        midNode.left = leftNode
        midNode.right = rightNode

        return midNode

    def buildTree(self, preorder, inorder):
        self.inorder = inorder
        self.preorder = preorder
        return self.toBuildTree(0, len(self.inorder), 0, len(self.preorder))

if __name__ == "__main__":
    s = Solution()

    n = s.buildTree([1, 2, 3], [1, 2, 3])
