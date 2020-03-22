/Runtime: 68 ms, faster than 32.66% of JavaScript online submissions for Maximum Depth of Binary Tree.
/Memory Usage: 37.1 MB, less than 62.50% of JavaScript online submissions for Maximum Depth of Binary Tree.

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

var number = 0
var maxDepth = function(root) {
    if (root === null){
         return  0
    }else if(root !== null){
        return  1 + Math.max(maxDepth(root.left), maxDepth(root.right)); 
    }
};
