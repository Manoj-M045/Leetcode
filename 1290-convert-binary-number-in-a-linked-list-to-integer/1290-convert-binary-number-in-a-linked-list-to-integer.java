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
        ListNode temp=head;
        int c=0,sum=0;
        int power;
        while(temp!=null){
            temp=temp.next;
            c++;
        }
        ListNode curr=head;
        power=c-1;
        while(curr!=null){
            sum=sum+(curr.val*(int)Math.pow(2,power));
            power--;
            curr=curr.next;
        }
        return sum;
        
    }
}