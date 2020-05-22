//Runtime: 12 ms, faster than 7.99% of Go online submissions for Path Sum.
//Memory Usage: 4.8 MB, less than 100.00% of Go online submissions for Path Sum.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, sum int) bool {
    if root == nil{
        return false
    }
    sum -= root.Val
    
    if root.Left == nil && root.Right == nil && sum == 0 {
        return true
    }
    return hasPathSum(root.Left, sum) || hasPathSum(root.Right, sum)
}
