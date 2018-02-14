import unittest

from anagram_count import anagram_count


class AnagramCountTests(unittest.TestCase):
    def test_detect_no_change_chars(self):
        self.assertEqual(anagram_count("abc", "abc"), 1)

    def test_detect_anagrams_of_self(self):
        self.assertEqual(anagram_count('aab', 'baa'), 1)

    def test_child_anagrams(self):
        self.assertEqual(anagram_count('AbrAcadAbRa', 'cAda'), 2)

    def test_child_anagrams_2(self):
        self.assertEqual(anagram_count('AdnBndAndBdaBn', 'dAn'), 4)

    def test_should_not_fail_with_larger_child(self):
        self.assertEqual(anagram_count('test', 'testing'), 0)

if __name__ == '__main__':
    unittest.main()