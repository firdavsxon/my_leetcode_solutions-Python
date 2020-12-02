"""
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what
you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes
to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.
"""


# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def rearrangeLastN(l, n):
    dummy = temp = ListNode(0)
    current, current2  = l, l
    r = reverse(current)

    for i in range(n):
        temp.next = ListNode(r.value)
        r = r.next
        temp = temp.next

    rev1 = reverse(dummy.next)
    rev2 = reverse(r)
    out = merging_list(list1=rev1, list2=rev2)
    return out



def reverse(root):
    prev = None
    while root:
        temp = root.next
        root.next = prev
        prev = root
        root = temp
    return prev

def merging_list(list1,list2):
    dummy_node = tail = ListNode(0)
    while list1:
        tail.next = ListNode(list1.value)
        list1 = list1.next
        tail = tail.next
    while list2:
        tail.next = ListNode(list2.value)
        list2 = list2.next
        tail = tail.next
    return dummy_node.next


def print_root(root):
    if not root:
        print("Sorry no data")
    current = root
    while current:
        print(current.value, end=" -> ")
        current = current.next

def rearrangeLastN1(l, n):
    if n == 0:
        return l
    front, back = l, l
    for _ in range(n):
        front = front.next
    if not front:
        return l
    while front.next:
        front = front.next
        back = back.next
    out = back.next
    back.next = None
    front.next = l
    return out



def main():
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)

    print_root(root)

    print()
    print()
    # rearrangeLastN(root, 3)
    print_root(rearrangeLastN1(root, 3))



main()


