from linked_list import LLNode, create_LL, listify_LL


def add_2_nums_reverse(head1, head2):
    new = LLNode()
    curr = new
    c1, c2 = head1, head2
    carry = 0
    while c1 or c2:
        total = (c1.val if c1 else 0) + (c2.val if c2 else 0) + carry
        if c1:
            c1 = c1.next
        if c2:
            c2 = c2.next
        carry = total // 10
        curr.next = LLNode(total % 10)
        curr = curr.next
    if carry != 0:
        curr.next = LLNode(carry)
    return new.next


import unittest


class TestAdd2NumsReverse(unittest.TestCase):

    def test_equal_sizes(self):
        added = add_2_nums_reverse(create_LL([1, 2, 3]), create_LL([4, 5, 6]))
        self.assertEqual(
            listify_LL(added),
            [5, 7, 9]
        )

    def test_unequal_sizes(self):
        added = add_2_nums_reverse(create_LL([4, 5, 7]), create_LL([1]))
        self.assertEqual(
            [5, 5, 7],
            listify_LL(added)
        )

    def test_carry_unequal(self):
        added = add_2_nums_reverse(create_LL([4, 9, 9]), create_LL([9]))
        self.assertEqual(
            [3, 0, 0, 1],
            listify_LL(added)
        )

    def test_carry_nines(self):
        added = add_2_nums_reverse(create_LL([9, 9, 9]), create_LL([1]))
        self.assertEqual(
            [0, 0, 0, 1],
            listify_LL(added)
        )


if __name__ == '__main__':
    unittest.main()
