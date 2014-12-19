# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None:
            return []

        dfs_list = list()
        ret = []
        dfs_list.append(root)


        while len(dfs_list) > 0:
            e = dfs_list.pop()
            if type(e) is int :
                ret.append(e)
            else:
                dfs_list.append(e.val)
                if e.right is not None:
                    dfs_list.append(e.right)
                if e.left is not None:
                    dfs_list.append(e.left)
        return ret

if __name__ == "__main__":
    print Solution().postorderTraversal(TreeNode(-1))