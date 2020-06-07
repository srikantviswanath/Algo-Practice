from linked_list import LLNode, print_LL, reverse_LL


def intertwine_from_end(head: LLNode) -> LLNode:
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    head2 = reverse_LL(slow)
    return intertwine(head, head2)


def intertwine(head1: LLNode, head2: LLNode) -> LLNode:
    if not head1:
        return head2
    if not head2:
        return head1
    anchor = head1
    while head1 and head2:
        temp = head1.next
        head1.next = head2
        head1 = temp

        temp = head2.next
        head2.next = head1
        head2 = temp
    if head1 is not None:
        head1.next = None
    return anchor


if __name__ == '__main__':
    head = LLNode(1)
    head.next = LLNode(2)
    head.next.next = LLNode(3)
    head.next.next.next = LLNode(4)
    head.next.next.next.next = LLNode(5)

    print_LL(intertwine_from_end(head))