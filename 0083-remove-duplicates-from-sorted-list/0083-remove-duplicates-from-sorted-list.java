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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode tptr=head;
        LinkedList<Integer> numbers = new LinkedList<>();
        while(tptr!=null)
        {
            if(!(numbers).contains(tptr.val))
            {   
                numbers.add(tptr.val);
            }
            tptr=tptr.next;

        }
        Collections.sort(numbers);
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        for (int num : numbers) {
            current.next = new ListNode(num);
            current = current.next;
        }
        return dummy.next;
        
    }
}