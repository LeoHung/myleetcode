# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if( root == None):
            return []

        tra_list = []

        tra_list.append( [root, False])

        ret = []

        while(len(tra_list) > 0):
            node, isVisisted = tra_list[-1][0], tra_list[-1][1]
            if(isVisisted):
                ret.append(node.val)
                tra_list.pop()
            else:
                tra_list[-1][1] = True
                if( node.right != None):
                    tra_list.append( [node, False])
                if( node.left != None):
                    tra_list.append([node, False])
        return ret

