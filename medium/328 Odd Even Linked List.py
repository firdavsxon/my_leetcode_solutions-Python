"""

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL  1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL  2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> Optional[ListNode]:
        if head is None:
            return None


        current = head
        prev = None
        temp = []

        while current.next:
            prev = current
            if current.next:
                temp.append(current.next.val)
            current = current.next.next
            prev.next = current
            if not current:
                break
        if prev and prev.next:
            prev=prev.next

        while temp:
            prev.next = ListNode(temp.pop(0))
            prev = prev.next
        return head




    def p(self, root):
        cur = root
        while cur:
            print(cur.val, end="->")
            cur=cur.next




def main():
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    root.next.next.next.next.next = ListNode(6)
    root.next.next.next.next.next.next = ListNode(7)
    root.next.next.next.next.next.next.next = ListNode(8)
    test = Solution()
    test.p(root)
    test.oddEvenList(root)

    print()
    test.p(root)


main()


