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
    public ListNode middleNode(ListNode head) {
        int c=0,i=0;
        int middle;
        ListNode curr=head;
        while(curr!=null){
            c++;
            curr=curr.next;
        }
        middle=c/2;
        ListNode temp=head;
        while(i<middle){
           temp=temp.next;
           i++;
        }
        return temp;
    }
}

