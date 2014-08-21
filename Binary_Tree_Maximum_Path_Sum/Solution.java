/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.lang.*;
class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode(int x) { val = x; }
}

public class Solution {


    public int max;

    public int maxPathSum(TreeNode root) {
        this.max = root.val;
        traversePathSum(root);
        return this.max;
    }

    public int traversePathSum(TreeNode root){
        int retVal;
        if(root.left == null && root.right == null){
            retVal = root.val;

            this.max = Math.max(this.max, retVal);
        }else if(root.left == null && root.right != null){
            int maxRight = traversePathSum(root.right);
            retVal = Math.max(root.val, root.val + maxRight);

            this.max = Math.max(this.max, retVal);
        }else if(root.right == null && root.left != null){
            int maxLeft = traversePathSum(root.left);
            retVal = Math.max(root.val, root.val + maxLeft);

            this.max = Math.max(this.max, retVal);
        }else{
            int maxRight = traversePathSum(root.right);
            int maxLeft = traversePathSum(root.left);
            retVal = root.val;
            retVal = Math.max(retVal, root.val + maxRight);
            retVal = Math.max(retVal, root.val + maxLeft);

            this.max = Math.max(this.max, root.val);
            this.max = Math.max(this.max, root.val + maxRight);
            this.max = Math.max(this.max, root.val + maxLeft);
            this.max = Math.max(this.max, root.val + maxRight + maxLeft);
        }

        return retVal;
    }

    public static void main(String[] argv){
        TreeNode root = new TreeNode(1);
        TreeNode left_node = new TreeNode(2);
        TreeNode right_node = new TreeNode(3);

        root.left = left_node;
        root.right = right_node;

        Solution s = new Solution();

        System.out.println(s.maxPathSum(root));

    }


}
