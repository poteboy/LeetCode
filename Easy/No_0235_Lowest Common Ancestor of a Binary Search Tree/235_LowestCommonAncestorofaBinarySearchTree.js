//Runtime: 68 ms, faster than 97.18% of JavaScript online submissions for Lowest Common Ancestor of a Binary Search Tree.
//Memory Usage: 43.7 MB, less than 80.00% of JavaScript online submissions for Lowest Common Ancestor of a Binary Search Tree.

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    if (p.val < root.val && q.val < root.val){
        return lowestCommonAncestor(root.left, p,q);
    }else if(p.val > root.val && q.val > root.val){
        return lowestCommonAncestor(root.right, p, q);
    }else{
        return root;
    }
};
