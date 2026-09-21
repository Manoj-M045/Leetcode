/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int i=0,sum=0,len=0;
        ListNode tptr=head;
        while(tptr!=null)
        {
            len++;
            tptr=tptr.next;
        }
        tptr=head;
        while(tptr!=null)
        {
           sum=sum+tptr.val*(int)Math.pow(2,len-1-i);
           tptr=tptr.next;
           i++;
        }
        return sum;
        
    }
}