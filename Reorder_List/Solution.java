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

    public void printFoward(ListNode head){
        System.out.println(head.val);
        if(head.next != null){
            printFoward(head.next);
        }
    }

    public ListNode split2twoList(ListNode head){
        ListNode fast_runner= head;
        ListNode slow_runner= head;
        ListNode next_head = null;

        while(fast_runner != null){
            if(fast_runner.next != null && fast_runner.next.next != null ){
                fast_runner = fast_runner.next.next;
                slow_runner = slow_runner.next;
            }else{
                break;
            }
        }
        // split
        next_head = slow_runner.next;
        slow_runner.next = null;

        return next_head;
    }

    public ListNode reverse(ListNode head){
        ListNode current_n=null;
        ListNode prev_n=null;
        ListNode next_n=null;

        if(head == null){return null;}

        prev_n = head;
        current_n = head.next;

        while(current_n != null){
            next_n = current_n.next;
            current_n.next = prev_n;

            // head case
            if(prev_n == head){
                prev_n.next = null;
            }

            // next step
            prev_n = current_n;
            current_n = next_n;
        }


        return prev_n;
    }

    public ListNode merge2list(ListNode head_1, ListNode head_2){
        ListNode n1 = head_1;
        ListNode n2 = head_2;

        if(n2 == null){return head_1;}

        while(n2 != null){
            ListNode n1_next = n1.next;
            ListNode n2_next = n2.next;
            n1.next = n2;
            n2.next = n1_next;

            n1 = n1_next;
            n2 = n2_next;
        }
        return head_1;
    }

    public void reorderList(ListNode head) {
        if(head == null){return ;}

        ListNode n2_head = split2twoList(head);

        n2_head = reverse(n2_head);

        merge2list(head, n2_head);
    }


    public static void main(String[] argv){
        ListNode n=null;
        ListNode current= null;
        int[] values = new int[]{1};
        for(int i = 0; i < values.length; i++){
            if(i ==0){
                n = new ListNode(values[i]);
                current = n;
            }

            if(i < values.length-1){
                current.next = new ListNode(values[i+1]);
                current = current.next;
            }
        }

        Solution s = new Solution();

        // s.printFoward(n);
        s.reorderList(n);
        s.printFoward(n);

    }
}
