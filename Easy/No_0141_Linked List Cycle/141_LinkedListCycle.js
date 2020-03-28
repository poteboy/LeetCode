
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

class ListNode{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

var node1 = new ListNode(3)
var node2 = new ListNode(2)
var node3 = new ListNode(0)
var node4 = new ListNode(-4)
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node2;

console.log(hasCycle(node1));
