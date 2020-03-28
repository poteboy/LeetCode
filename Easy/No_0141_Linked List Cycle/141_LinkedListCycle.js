
//Runtime: 68 ms, faster than 52.00% of JavaScript online submissions for Linked List Cycle.
//Memory Usage: 36.8 MB, less than 68.75% of JavaScript online submissions for Linked List Cycle.


/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    if (head === null){
        return false;
    }
    var fast = head;
    var slow = head;
    // javascriptではorは||で表す。if not は!で表す。
    while (slow !== null){
        if(!fast.next || !fast.next.next){
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
        if (fast === slow){
            return true
        }
    }
    return false;
};
