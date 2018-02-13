import unittest
import find_diff from find_diff


class TestFindDiff(unittest.TestCase):

    def test_find_diff_raises_type_error_on_none(self):
        with self.assertRaises(TypeError):
            find_diff(None, "aabbss")

    def test_find_diff(self):
        self.assertEqual(find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(find_diff('aaabbcdd', 'abdbacade'), 'e')

    def test_find_diff_returns_empty_str_with_similar_inputs(self):
        self.assertEqual(find_diff("aabbcc", "aabbcc"), "")


if __name__ == "__main__":
    unittest.main()
