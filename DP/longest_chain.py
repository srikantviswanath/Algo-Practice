def longest_chain_top_down(words):
    word_set = set(words)
    out = 0
    cache = {}

    def helper(word):
        if word == '':
            return 1 if word in word_set else 0
        local_max = 0
        for i in range(len(word)):
            new = word[:i] + word[i+1:]
            if new in word_set:
                if new in cache:
                    count = cache[new]
                else:
                    count = helper(new)
                local_max = max(local_max, count)
        cache[word] = local_max + 1
        return cache[word]

    for word in words:
        out = max(out, helper(word))
    return out

if __name__ == '__main__':
    words = ['b', 'a', 'ba', 'bca', 'bda', 'bdca', 'xyzabc', '']
    print(longest_chain_top_down(words))