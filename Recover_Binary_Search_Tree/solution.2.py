# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node

    def check(self, cur):
        if self.last is None:
            self.last = cur 
        else:
            if cur.val < self.last.val:
                return cur 
            self.last = cur
        return None

    def left_right(self, cur):
        if cur.left is None:
            return cur
        else:
            p = cur.left
            while not(p.right == None or p.right == cur):
                p = p.right 
            return p

    def recoverTree(self, root):
        self.last = None

        # Morris Traversal 
        p1, p2 = None, None

        cur = root

        while cur is not None:
            if cur.left == None:
                tmp = self.check(cur)
                if tmp is not None:
                    if p1 is None:
                        p1 = self.last
                        p2 = cur
                    else:
                        p2 = tmp
                cur = cur.right 
            else:
                lr_p = self.left_right(cur)
                if lr_p.right == cur:
                    lr_p.right = None

                    tmp = self.check(cur)
                    if tmp is not None:
                        if p1 is None:
                            p1 = self.last
                            p2 = cur
                        else:
                            p2 = tmp       

                    cur = cur.right
                else:
                    lr_p.right = cur
                    cur = cur.left
        
        if p1 is None:
            return root

        # swap value
        if p2 is None:
            if p1.left is not None and p1.val < p1.left.val: 
                p2 = p1.left
            elif p1.right is not None and p1.right.val < p1.val:
                p2 = p1.right

        p1.val, p2.val = p2.val, p1.val

        return root 

def inorder(node):
    if node is None:
        return 
    inorder(node.left)
    print node.val
    inorder(node.right)

if __name__ == "__main__":
    root = TreeNode(2)
    root.right = TreeNode(1)

    root = Solution().recoverTree(root)
    inorder(root)