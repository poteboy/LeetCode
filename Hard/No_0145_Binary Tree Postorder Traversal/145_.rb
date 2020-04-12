#Runtime: 36 ms, faster than 39.06% of Ruby online submissions for Binary Tree Postorder Traversal.
#Memory Usage: 9.4 MB, less than 100.00% of Ruby online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def postorder_traversal(root)
    curr = []
    return helper(root, curr)
end


def helper(root, curr)
    if root
        helper(root.left, curr)
        helper(root.right, curr)
        curr.push root.val
    end
    return curr
end
    
