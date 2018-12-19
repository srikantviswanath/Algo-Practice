import unittest
from linked_list import create_LL, listify_LL, LLNode

def add_2_nums_helper(head1, head2):
    if not head1 and not head2:
        return None, 0
    next_node, carry = add_2_nums_helper(head1.next, head2.next)
    curr_total = head1.val + head2.val + carry
    curr_node = LLNode(curr_total % 10)
    curr_node.next = next_node
    return curr_node, curr_total // 10


def pad_zeros_to_smaller_num(head1, head2):
    n1, n2 = 0, 0
    alias1, alias2 = head1, head2
    while head1:
        n1 += 1
        head1 = head1.next
    while head2:
        n2 += 1
        head2 = head2.next
    if n1 == n2:
        return alias1, alias2
    small, big = alias1 if n1 < n2 else alias2, alias1 if n1 > n2 else alias2
    diff = abs(n1 - n2)
    head = curr = LLNode()
    while diff:
        curr.next = LLNode(0)
        curr = curr.next
        diff -= 1
    curr.next = small
    return head.next, big


def add_2_nums(head1, head2):
    head1, head2 = pad_zeros_to_smaller_num(head1, head2)
    head, carry = add_2_nums_helper(head1, head2)
    if carry != 0:
        node = LLNode(carry)
        node.next = head
        return node
    return head

#
class Add2NumsTest(unittest.TestCase):

    def test_eq_digits(self):
        num1 = create_LL([9, 9, 9])
        num2 = create_LL([9, 9])
        self.assertListEqual(
            listify_LL(add_2_nums(num1, num2)),
            [1, 0, 9, 8]
        )


if __name__ == '__main__':
    unittest.main()