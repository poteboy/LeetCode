#Runtime: 36 ms, faster than 61.90% of Ruby online submissions for Delete Node in a Linked List.
#Memory Usage: 9.5 MB, less than 100.00% of Ruby online submissions for Delete Node in a Linked List.

def delete_node(node)
    if node.next != nil
        node.val = node.next.val
        node.next = node.next.next
    end
end
