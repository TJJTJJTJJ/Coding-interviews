/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        // 根节点为空或者前序和中序数组长度不一致
        if (pre==null || in==null){
            return null;
        }
        
        if (pre.length!=in.length){
            throw new IllegalArgumentException("Invalid input1!");
        }
        // 正常情况
        int n = pre.length;
        return constructBinaryTree(pre, 0, n-1, in, 0, n-1);
    }
    TreeNode constructBinaryTree(int [] pre, int startPre, int endPre, int [] in, int startIn, int endIn){
        // 正常结束条件，分为只剩一个元素或者一个元素都没有。
        TreeNode root = new TreeNode(pre[startPre]);
        if(startPre==endPre && startIn==endIn && pre[startPre]==in[startPre]){
            root.left = null;
            root.right = null;
            return root;
        }
        // 序列不匹配时，在递归的过程中一定会发生在当前root结点对应的值在in中没有。
        int inOrder=0;
        int flag = 1;
        for (inOrder=startIn; inOrder<=endIn; inOrder++) {
            if (pre[startPre]==in[inOrder]){
                flag=0;
                break;
            }            
        }
        if (flag==1){
            throw new IllegalArgumentException("Invalid input2!");
        }
        
        int len = inOrder-startIn;
        // 左子树
        if(len==0){
            root.left=null;
        }
        else{
            root.left = constructBinaryTree(pre, startPre+1, startPre+len, in, startIn, startIn+len-1);
        }
        // 右子树
        if (inOrder==endIn){
            root.right=null;
        }
        else{
            root.right = constructBinaryTree(pre, startPre+len+1, endPre, in, startIn+len+1, endIn);
        }
        return root;
    }
}

##

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        // 根节点为空或者前序和中序数组长度不一致
        if (pre==null || in==null){
            return null;
        }
        
        if (pre.length!=in.length){
            throw new IllegalArgumentException("Invalid input1!");
        }
        // 正常情况
        int n = pre.length;
        return constructBinaryTree(pre, 0, n-1, in, 0, n-1);
    }
    TreeNode constructBinaryTree(int [] pre, int startPre, int endPre, int [] in, int startIn, int endIn){
        // 正常结束条件，分为只剩一个元素或者一个元素都没有。
        if(endPre-startPre==-1 && endIn-startIn==-1){
            return null;
        }
        TreeNode root = new TreeNode(pre[startPre]);
        if(startPre==endPre && startIn==endIn && pre[startPre]==in[startPre]){
            root.left = null;
            root.right = null;
            return root;
        }
        
        // 序列不匹配时，在递归的过程中一定会发生在当前root结点对应的值在in中没有。
        int inOrder=0;
        int flag = 1;
        for (inOrder=startIn; inOrder<=endIn; inOrder++) {
            if (pre[startPre]==in[inOrder]){
                flag=0;
                break;
            }            
        }
        if (flag==1){
            throw new IllegalArgumentException("Invalid input2!");
        }
        
        int len = inOrder-startIn;
        // 左子树
        root.left = constructBinaryTree(pre, startPre+1, startPre+len, in, startIn, startIn+len-1);
        root.right = constructBinaryTree(pre, startPre+len+1, endPre, in, startIn+len+1, endIn);
        return root;
    }
}