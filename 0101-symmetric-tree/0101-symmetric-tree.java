/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        TreeNode lef=root.left;
        TreeNode rig=root.right;
        return fun(lef,rig);   
    }
    static boolean fun(TreeNode lef,TreeNode rig){
        boolean l=true;
        boolean r=true;

        if(lef==null && rig==null){
            return true;
        }
        else if((lef==null && rig!=null)||(lef!=null && rig==null)){
            return false;
        }
        else if(lef.val!=rig.val){
            return false;
        }
        l=fun(lef.left,rig.right);
        r=fun(lef.right,rig.left);

        return l&&r;
    }
}