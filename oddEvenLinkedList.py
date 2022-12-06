from typing import Optional, ListNode


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    currentOdd = head
    count = 2
    node = head
    pre = node
    node = node.next
    while node is not None:
        if count % 2 == 0:
            pre = node
            node = node.next
        else:
            next = node.next
            pre.next = next
            temp = currentOdd.next
            currentOdd.next = node
            node.next = temp
            currentOdd = node
            node = next
        count += 1
    return head
