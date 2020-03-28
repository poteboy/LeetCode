//Runtime: 44 ms, faster than 98.48% of JavaScript online submissions for Invert Binary Tree.
//Memory Usage: 33.7 MB, less than 100.00% of JavaScript online submissions for Invert Binary Tree.


/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root === null){
        return null;
    }
    var tmp = root.left
    root.left = root.right;
    root.right = tmp
    invertTree(root.left)
    invertTree(root.right)
    return root
};
