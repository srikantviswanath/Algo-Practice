from collections import Counter
import unittest


def find_permutation(string, pattern):
	"""
	Given a larger len string and a smaller `pattern`, find if there is any permutation of `pattern` in `string`
	:param string:
	:param pattern:
	:return:
	"""
	if not string or len(pattern) > len(string):
		return False
	if not pattern:
		return True
	P, S = len(pattern), len(string)
	pattern_counter = Counter(pattern)
	diff = Counter(pattern)
	for idx, char in enumerate(string[: S - P + 1]):
		if not diff:
			return True
		if idx == 0:
			diff = pattern_counter - Counter(string[: P])
		else:
			prev = string[idx - 1]
			new = string[idx + P - 1]
			if prev in pattern_counter:
				diff[prev] = diff.get(prev, 0) + 1
			if new in pattern_counter:
				diff[new] -= 1
				if diff[new] <= 0:
					del diff[new]
	return not bool(diff)



class TestFindPermutation(unittest.TestCase):

	def test_empty_string(self):
		self.assertFalse(find_permutation('', 'abc'))

	def test_pattern_smaller_than_string(self):
		self.assertFalse(
			find_permutation('asd', 'qwerree')
		)

	def test_empty_pattern(self):
		self.assertTrue(find_permutation('asdf', ''))

	def test_pattern_present_in_string(self):
		self.assertTrue(find_permutation('acdefagaik', 'gfae'))

	def test_pattern_not_present_in_string(self):
		self.assertFalse(find_permutation('acdefagaik', 'gafi'))


if __name__ == '__main__':
	unittest.main()