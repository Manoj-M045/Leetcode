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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0,head);
        ListNode temp=head;
        ListNode curr=dummy;
        int len=0;
        while(temp!=null){
            len++;
            temp=temp.next;
        }
        int x=len-n;
        int i=0;
        while(i<x){
            curr=curr.next;
            i++;
        }
        curr.next=curr.next.next;
        return dummy.next;    
        
    }
}