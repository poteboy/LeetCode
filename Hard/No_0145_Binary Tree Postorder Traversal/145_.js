
//Runtime: 52 ms, faster than 79.50% of JavaScript online submissions for Binary Tree Postorder Traversal.
//Memory Usage: 33.8 MB, less than 50.00% of JavaScript online submissions for Binary Tree Postorder Traversal.


/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    let curr = [];
    return helper(root, curr)
    
};

var helper = function(root, curr){
    if(root){
        helper(root.left, curr);
        helper(root.right, curr);
        curr.push(root.val);
    }
    return curr
}
