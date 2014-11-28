# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # end not included
    def genTrees(self, start, end):
        ret = []

        if( end == start ):
            return [ None]

        if(end - start == 1 ):
            return [ TreeNode(start) ]

        for mid in xrange(start, end):
            left_trees = self.genTrees(start, mid)
            right_trees = self.genTrees( mid+1, end)
            for lt in left_trees:
                for rt in right_trees:
                    mid_node = TreeNode(mid)
                    mid_node.left = lt
                    mid_node.right = rt
                    ret.append(mid_node)

        return ret

    # @return a list of tree node
    def generateTrees(self, n):
        return self.genTrees(1, n+1)
