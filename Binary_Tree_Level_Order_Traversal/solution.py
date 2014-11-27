# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        # do BFS
        q = list()
        q.append(root)
        q.append(None)

        ret = []
        tmp_row = []
        while len(q) > 0:
            node = q.pop(0)
            if(node == None):
                if len(tmp_row) > 0:
                    ret.append(tmp_row)
                    tmp_row = []
                    q.append(None)
                    continue
                else:
                    break

            tmp_row.append(node.val)
            if not node.left == None:
                q.append(node.left)
            if not node.right == None:
                q.append(node.right)

        return ret

if __name__ == "__main__":
    s = Solution()

    t_n = TreeNode(3)
    t_1 = TreeNode(9)
    t_n.left = t_1
    t_2 = TreeNode(20)
    t_n.right = t_2
    t_3 = TreeNode(15)
    t_2.left = t_3
    t_4 = TreeNode(7)
    t_2.right = t_4

    print s.levelOrder(t_n)
