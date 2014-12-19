# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum_v):
        if root == None:
            return []
        
        ret = []
        cache = []
        sum_v = sum_v
        self.dfs(root, cache, ret, sum_v)
        return ret

    def dfs(self, node, cache, ret, sum_v):
        
        cache.append(node.val)

        if node.left is None and node.right is None:
            if sum(cache) == sum_v:
                ret.append(list(cache))
        elif node.left is None and node.right is not None:
            self.dfs(node.right, cache, ret, sum_v)
        elif node.right is None and node.left is not None:    
            self.dfs(node.left, cache, ret, sum_v)
        else:
            self.dfs(node.right, cache, ret, sum_v)
            self.dfs(node.left, cache, ret, sum_v)

        cache.pop()


