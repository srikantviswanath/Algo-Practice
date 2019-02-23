from linked_list import DoubleLLNode, listify_LL
import unittest


class LRUCache(object):
    """
    Implementation of least recently used cache using a doubly linked list. This cache offers the following:
    - put(key, value): O(1)
    - get(key, value): O(1)
    without keeping track of access/put times.

    **NOTE: New elements that are put in the cache but not yet looked up are considered the same priority as least
    recently used
    """

    def __init__(self, max_size: int=5):
        self.max_size = max_size
        self.cache = {}
        self._head = None
        self._tail = None

    @property
    def cache_size(self):
        return len(self.cache)

    def put(self, key: str, value: object) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
        else:
            if self.cache_size == self.max_size:
                self._shrink_cache()
            new_node = DoubleLLNode(key, value)
            self.cache[key] = new_node
            if self.cache_size == 1:
                self._head = self._tail = new_node
            else:
                self._insert_at_head(new_node)

    def _insert_at_tail(self, node: DoubleLLNode) -> None:
        self._tail.next = node
        node.prev = self._tail
        self._tail = self._tail.next

    def _insert_at_head(self, node: DoubleLLNode) -> None:
        node.next = self._head
        self._head.prev = node
        self._head = self._head.prev

    def _shrink_cache(self):
        node = self._head
        self._head = node.next
        node.next = None
        self._head.prev = None
        self.cache.pop(node.key)

    def get(self, key: str) -> object:
        node = self.cache[key]
        if self._tail is node:
            return node.val
        if self._head is node:
            self._head = node.next
            node.next.prev = None
            node.next = None
            self._insert_at_tail(node)
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = None
            node.next = None
            self._insert_at_tail(node)
        return node.val

    def __str__(self):
        return str(listify_LL(self._head))


class TestLRUCache(unittest.case.TestCase):

    def setUp(self):
        self.cache = LRUCache()

    def test_emptyCache_putOneElement(self):
        self.cache.put('a', 'apple')
        self.assertEqual(self.cache.cache_size, 1)
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_cacheSizeLessThanLimit_duplicatedPuts_multipleGets(self):
        self.cache.put('a', 'apple')
        self.cache.put('b', 'banana')
        self.cache.put('a', 'apricot')
        self.cache.put('c', 'cantaloupe')

        self.assertEqual(self.cache.get('a'), 'apricot')
        self.assertEqual(self.cache.get('c'), 'cantaloupe')
        self.assertEqual(self.cache.get('b'), 'banana')
        self.assertEqual(self.cache.cache_size, 3)
        self.assertListEqual(listify_LL(self.cache._head), ['apricot', 'cantaloupe', 'banana'])

        self.assertEqual(self.cache._head.key, 'a')
        self.assertEqual(self.cache._tail.key, 'b')

    def test_cacheSizeExceeds(self):
        self.cache.put('a', 'apple')
        self.cache.put('b', 'banana')
        self.cache.put('a', 'apricot')
        self.cache.put('c', 'cantaloupe')
        self.cache.put('d', 'durien')
        self.cache.put('e', 'elephant fruit')
        self.cache.get('b')
        self.cache.get('d')
        self.cache.put('f', 'fruit')

        with self.assertRaises(KeyError):
            self.cache.get('e')

        self.assertEqual(self.cache.cache_size, 5)
        self.assertListEqual(listify_LL(self.cache._head), ['fruit', 'cantaloupe', 'apricot', 'banana', 'durien'])
        self.assertEqual(self.cache.get('f'), 'fruit')
        self.assertListEqual(listify_LL(self.cache._head), ['cantaloupe', 'apricot', 'banana', 'durien', 'fruit'])

    def test_getMostRecentlyUsed_element(self):  # accessing the head of the linked list
        self.cache.put('a', 'apple')
        self.cache.put('b', 'banana')
        self.cache.put('a', 'apricot')
        self.cache.put('c', 'cantaloupe')
        self.cache.put('d', 'durien')
        self.cache.put('e', 'elephant fruit')
        self.cache.get('b')
        self.cache.get('d')
        self.cache.put('f', 'fruit')

        self.assertEqual(self.cache.get('d'), 'durien')




if __name__ == '__main__':
    unittest.main()
