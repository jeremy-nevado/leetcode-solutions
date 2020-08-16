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

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode p = l1, q = l2;
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (p != null || q != null) {
          if (p.val >= q.val) {
            curr.next = new ListNode(p.val);
            curr = curr.next;
            p = p.next;
          } else {
            curr.next = new ListNode(q.val);
            curr = curr.next;
            q = q.next;
          }
        }
      if (q != null) {
        curr.next = q;
      } else {
        curr.next = p;
      }
      return dummy.next;
    }

    public static void main(String[] args) {
    Solution sol = new Solution();
    ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(3)));
    ListNode l2 = new ListNode(0, new ListNode(4, new ListNode(5)));
    System.out.println(sol.mergeTwoLists(l1, l2));
  }
}