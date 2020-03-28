
//Runtime: 68 ms, faster than 62.69% of JavaScript online submissions for Linked List Cycle II.
//Memory Usage: 36.8 MB, less than 31.25% of JavaScript online submissions for Linked List Cycle II.

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
var detectCycle = function(head) {
    if (!head){
        return null;
    }
    var slow = head;
    var fast = head;
    while (slow !== null){
        if (!fast.next || !fast.next.next){
            return null;
        } 
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast){
            break
        }
        //ここまでで、この線形リストがサイクルであることが分かった。
        //また、slowとfastはサイクルの中で出会う（サイクル以前に戻る事はありえない為）
        //headはスタート地点にあり、slow（でなくてもいいが、サイクルの中にある任意の点）を同時に進ませれば、混ざりあうのはサイクルがスタートする点だけ
    }
    while(head !== slow){
        head = head.next;
        slow = slow.next;
    }
    return head
};
