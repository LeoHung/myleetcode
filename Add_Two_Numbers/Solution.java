/**
 * Definition for singly-linked list.
 * public class ListNode {
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1==null && l2 == null){return null;}

        ListNode ans_l= new ListNode(0);
        ListNode o_ans_l = ans_l;
        int isOverflow = 0;

        boolean isFirst= true;

        ListNode l1Ptr= l1, l2Ptr=l2 ;

        while( l1Ptr != null || l2Ptr != null){
            // System.out.println(l1Ptr);
            // System.out.println(l2Ptr);

            int l1_val=0, l2_val=0, sum_val=0;
            if(l1Ptr != null){
                l1_val = l1Ptr.val;
                l1Ptr = l1Ptr.next;
            }
            if(l2Ptr != null){
                l2_val = l2Ptr.val;
                l2Ptr = l2Ptr.next;
            }

            sum_val = l1_val + l2_val + isOverflow;

            if(sum_val >= 10){
                sum_val -= 10;
                isOverflow = 1;
            }else{
                isOverflow = 0;
            }
            ans_l.val = sum_val;

            if(l1Ptr !=null || l2Ptr !=null){
                ans_l.next = new ListNode(0);
                ans_l = ans_l.next;
            }
        }

        if(isOverflow==1){
            ans_l.next = new ListNode(1);
        }


        return o_ans_l;
    }

    public static void main(String[] argv){
        ListNode l1 = new ListNode(2);
        ListNode o_l1 = null;
        o_l1 = l1;

        l1.next = new ListNode(4);
        l1 = l1.next;
        l1.next = new ListNode(3);

        ListNode o_l2 = null;
        ListNode l2 = new ListNode(5);
        o_l2 = l2;

        l2.next = new ListNode(6);
        l2 = l2.next;
        l2.next = new ListNode(4);

        Solution s = new Solution();

        ListNode ans_l = s.addTwoNumbers(o_l1, o_l2);
        while(ans_l != null){
            System.out.print(ans_l.val);
            ans_l = ans_l.next;
        }
        System.out.println("");
    }
}
