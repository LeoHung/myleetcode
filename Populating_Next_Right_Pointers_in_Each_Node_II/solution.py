# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return 
        
        parents = list()
        parents.append(root)
        while len(parents) > 0:
            cur = parents
            parents = list()
            for i in xrange(len(cur)):
                n = cur[i]
                
                if i < len(cur) - 1:
                    n.next = cur[i+1]

                if n.left is not None:
                    parents.append(n.left)
                if n.right is not None:
                    parents.append(n.right)