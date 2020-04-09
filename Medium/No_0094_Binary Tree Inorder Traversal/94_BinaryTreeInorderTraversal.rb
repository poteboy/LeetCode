#Runtime: 32 ms, faster than 77.86% of Ruby online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 9.2 MB, less than 100.00% of Ruby online submissions for Binary Tree Inorder Traversal.


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
def inorder_traversal(root)
    @list = []
    inorder(root)
    @list
end

def inorder(root)
    if root != nil
        inorder(root.left)
        @list.push root.val
        inorder(root.right)
    end
end
