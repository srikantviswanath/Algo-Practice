"""
Write a function that takes an input string and a character set and returns the minimum-length substring which contains every letter of the character set at least once, in any order
If you don't find a match, return an empty string

Example:
Input: "aabbcb"
Alphabet: {'a', 'b', 'c'}
Output: "abbc"

Input: "aaaaaaaaaabbbbbbbbccccccccsbabbbccc"
Alphabet: {'a', 'b', 'c'}
Output: "csba"

Input: "aaaaaaaaaabbbbbbbbccccccccsbabbbccc"
Alphabet: {'a', 'b', 'c', 'f'}
Output: ""
"""

def min_substring(string, alphabet):
    """
    O(N) sliding window approach
    :param str string:
    :param set alphabet:
    :return str:
    """
    from collections import defaultdict
    if not string:
        return ''
    begin, end = 0, 0
    found = defaultdict(int)
    ans = string
    ever_found = False
    while end < len(string):
        while len(found) == len(alphabet):
            ever_found = True
            ans = string[begin: end] if end - 1 - begin < len(ans) else ans
            found[string[begin]] -= 1
            if found[string[begin]] == 0:
                found.pop(string[begin])
            begin += 1
        if string[end] in alphabet:
            found[string[end]] += 1
        end += 1
    return ans if ever_found else ""


if __name__ == '__main__':
    print(min_substring('aaaaaaaaaabbbbbbbbccccccccsbabbbccc', {'a', 'b', 'c'}))
