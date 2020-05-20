//Runtime: 4 ms, faster than 90.70% of Go online submissions for Maximum Depth of Binary Tree.
//Memory Usage: 4.7 MB, less than 83.33% of Go online submissions for Maximum Depth of Binary Tree.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil{
        return 0
    }
    count := 1 + max(maxDepth(root.Left), maxDepth(root.Right))
    return count
}

func max(a, b int)int {
    if a < b {
        return b
    }else {
        return a
    }
}
