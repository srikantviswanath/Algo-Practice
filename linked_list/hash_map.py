"""
Implement a hashmap using a linkedlist in case of key collisions
"""

class HashMapNode(object):

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __hash__(self):
        return self.hash(self.key)

    @staticmethod
    def hash(key):
        if not key:
            return 999
        return ord(key[0])


class HashMap(object):

    def __init__(self, size=16):
        self.size = size
        self.array = [None] * size

    def _get_hash_index(self, hashcode):
        return hashcode % self.size

    def __index__(self, key):
        self.get(key)

    def put(self, key, value):
        node = HashMapNode(key, value)
        index = self._get_hash_index(hash(node))
        if self.array[index] is None:
            self.array[index] = node
        else:
            head = self.array[index]
            found_node = self.traverse_chain(head, key)
            if found_node:
                found_node.value = value
            else:
                self.array[index] = node
                node.next = head

    def get(self, key):
        index = self._get_hash_index(HashMapNode.hash(key))
        if self.array[index] is None:
            raise KeyError
        head = self.array[index]
        found_node = self.traverse_chain(head, key)
        if found_node:
            return found_node.value

    def traverse_chain(self, head, key):
        while head:
            if head.key == key:
                return head
            head = head.next


import unittest


class TestHashMapNode(unittest.TestCase):

    def test_hash_non_empty(self):
        key = 'hello'
        node = HashMapNode(key, 'foo')
        self.assertEqual(HashMapNode.hash(key), 104)
        self.assertEqual(hash(node), 104)

    def test_hash_empty(self):
        key = ''
        node = HashMapNode(key, 'foo')
        self.assertEqual(HashMapNode.hash(key), 999)
        self.assertEqual(hash(node), 999)


class TestHashMap(unittest.TestCase):

    def test_put_in_empty_bucket(self):
        map = HashMap()
        key = 'vankai'
        map.put(key, 'koora')
        self.assertEqual(map.get(key), 'koora')

    def test_put_in_bucket_with_one_element(self):
        map = HashMap()
        map.put('vankai', 'koora')
        map.put('vengalappa', 'pulusu')
        self.assertEqual(map.get('vankai'), 'koora')
        with self.assertRaises(KeyError):
            map.get('burra')

    def test_get_key_not_present(self):
        map = HashMap()
        with self.assertRaises(KeyError):
            map.get('vankai')


    def test_update_key(self):
        map = HashMap()
        map.put('vankai', 'koora')
        map.put('tomato', 'pappu')
        map.put('velakkai', 'pacchadi')
        map.put('vankai', 'pulusu')
        self.assertEqual(map.get('vankai'), 'pulusu')


if __name__ == '__main__':
    unittest.main()
