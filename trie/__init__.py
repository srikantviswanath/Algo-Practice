class TrieNode(object):

    def __init__(self, char, end=False):
        self.char = char
        self.children = {}
        self.end = end


class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.end = True

    def prefix_search(self, prefix):
        root = self.root
        for char in prefix:
            pass


if __name__ == '__main__':
    phonebook = Trie()
    phonebook.insert('bald')
    phonebook.insert('build')
    print(phonebook)
