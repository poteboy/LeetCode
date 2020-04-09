# Runtime: 32 ms, faster than 78.38% of Ruby online submissions for Same Tree.
# Memory Usage: 9.5 MB, less than 100.00% of Ruby online submissions for Same Tree.




# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(p, q)
    return true if !p && !q
    return false if !p or !q
    if p and q && p.val == q.val
        left = is_same_tree(p.left, q.left)
        right = is_same_tree(p.right, q.right)
        return (left and right)
    end
    return false
end
