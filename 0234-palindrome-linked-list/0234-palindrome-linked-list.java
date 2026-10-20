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
    public boolean isPalindrome(ListNode head) {
        List<Integer>result=new ArrayList<>();
        List<Integer>res=new ArrayList<>();
        ListNode temp1=head;
        ListNode temp2=head;
        while(temp1!=null){
            result.add(temp1.val);
            temp1=temp1.next;
        }
        ListNode prev=null;
        ListNode curr=temp2;
        ListNode next=null;
        while(curr!=null){
          next=curr.next;
          curr.next=prev;
          prev=curr;
          curr=next;
        }
        while(prev!=null){
            res.add(prev.val);
            prev=prev.next;
        }
        return result.equals(res);
    }
}