
//Runtime: 68 ms, faster than 59.80% of JavaScript online submissions for Remove Duplicates from Sorted List.
//Memory Usage: 35.7 MB, less than 43.75% of JavaScript online submissions for Remove Duplicates from Sorted List.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    node = head;
    while (node !== null && node.next !== null){
        if(node.val === node.next.val){
            node.next = node.next.next;
            
        }else{
            node = node.next;
        }
    } 
    return head
};
