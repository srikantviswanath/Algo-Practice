class LLNode(object):

    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


class DoubleLLNode(LLNode):

    def __init__(self, key, val):
        super(DoubleLLNode, self).__init__(val)
        self.prev = None
        self.key = key


def create_LL(data_list):
    head = LLNode()
    curr = head
    for data in data_list:
        curr.next = LLNode(data)
        curr = curr.next
    return head.next


def print_LL(head):
    while head.next:
        print(head.val, '->', end='')
        head = head.next
    print(head.val)


def listify_LL(head):
    list_ = []
    while head:
        list_.append(head.val)
        head = head.next
    return list_


def reverse_LL(head):
    if not head:
        return
    prev = None
    while head:
        ahead = head.next
        head.next = prev
        prev = head
        head = ahead
    return prev


if __name__ == '__main__':
    head = create_LL([1, 2, 3, 4, 5, 6])
    print(listify_LL(head))