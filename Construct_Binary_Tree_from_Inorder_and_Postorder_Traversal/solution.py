# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    # right is not included
    def toBuildTree(self, inorder_left_i, inorder_right_i, postorder_left_i, postorder_right_i):

        if(inorder_right_i <= inorder_left_i or postorder_right_i <= postorder_left_i):
            return None



        midNodeValue = self.postorder[postorder_right_i-1]
        midNode = TreeNode(midNodeValue)

        inorder_mid_i = -1

        for i in range(inorder_left_i, inorder_right_i):
            if self.inorder[i] == midNodeValue:
                inorder_mid_i = i

        postorder_mid_i = postorder_left_i + (inorder_mid_i - inorder_right_i)

        new_inorder_left_left_i = inorder_left_i
        new_inorder_left_right_i = inorder_mid_i
        new_postorder_left_left_i = postorder_left_i
        new_postorder_left_right_i = postorder_left_i + (inorder_mid_i -inorder_left_i)

        leftNode = self.toBuildTree(
                        new_inorder_left_left_i,
                        new_inorder_left_right_i,
                        new_postorder_left_left_i,
                        new_postorder_left_right_i)

        new_inorder_right_left_i = inorder_mid_i+1
        new_inorder_right_right_i = inorder_right_i
        new_postorder_right_left_i = new_postorder_left_right_i
        new_postorder_right_right_i = postorder_right_i -1

        rightNode = self.toBuildTree(
                        new_inorder_right_left_i,
                        new_inorder_right_right_i,
                        new_postorder_right_left_i,
                        new_postorder_right_right_i
                    )

        midNode.left = leftNode
        midNode.right = rightNode

        return midNode

    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        return self.toBuildTree(0, len(self.inorder), 0, len(self.postorder))

if __name__ == "__main__":
    s = Solution()

    n = s.buildTree([2,1,3], [2,3,1])
