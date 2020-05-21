//Runtime: 0 ms, faster than 100.00% of Go online submissions for Same Tree.
//Memory Usage: 2.1 MB, less than 100.00% of Go online submissions for Same Tree.


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil && q == nil{
        return true
    } else if p == nil || q == nil || p.Val != q.Val{
        return false
    }else {
        return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
    }
    
}
