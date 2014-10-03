/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

 class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
       val = x;
       next = null;
    }
 }

public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null){ return false; }

        ListNode fast;
        ListNode slow;
        slow = fast = head;

        while(true){
            slow = slow.next;
            if(fast.next != null){
                fast = fast.next.next;
            }

            if(slow == null || fast == null || fast.next == null){
                return false;
            }

            if(slow == fast){
                return true;
            }
        }

    }
}
