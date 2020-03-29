//Runtime: 40 ms, faster than 99.93% of JavaScript online submissions for Reverse Linked List.
//Memory Usage: 34.9 MB, less than 86.96% of JavaScript online submissions for Reverse Linked List.

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
var reverseList = function(head) {
    var prev = null;
    var x = head;
    while (x !== null){
        var tmp = x.next;
        x.next = prev;
        prev = x;
        x = tmp
    }
    return prev;
    
};
