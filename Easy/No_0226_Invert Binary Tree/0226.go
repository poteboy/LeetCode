

//Runtime: 0 ms, faster than 100.00% of Go online submissions for Invert Binary Tree.
//Memory Usage: 2.2 MB, less than 33.33% of Go online submissions for Invert Binary Tree.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    
    if root == nil {
        return nil
    }
    root.Right, root.Left = root.Left, root.Right
    
    invertTree(root.Left)
    invertTree(root.Right)
    
    return root
    
}
