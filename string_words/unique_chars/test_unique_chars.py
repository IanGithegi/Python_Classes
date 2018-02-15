import unittest
from unique_chars import has_unique_chars
from string import ascii_lowercase, ascii_uppercase


class TestUniqueChars(unittest.TestCase):

    def test_none_input_returns_false(self):
        self.assertFalse(has_unique_chars(None))

    def test_empty_string_returns_true(self):
        self.assertFalse(has_unique_chars(""))

    def test_none_unique_characters_returns_false(self):
        self.assertFalse(has_unique_chars("foo"))

    def test_word_bar_returns_true(self):
        self.assertTrue(has_unique_chars("bar"))

    def test_word_amazing_returns_false(self):
        self.assertFalse(has_unique_chars("amazing"))

    def test_word_papa_returns_false(self):
        self.assertFalse(has_unique_chars("papa"))

    def test_word_rhythm_returns_false(self):
        self.assertFalse(has_unique_chars("rhythm"))

    def test_ascii_lowercase_returns_true(self):
        self.assertTrue(has_unique_chars(ascii_lowercase))

    def test_ascii_uppercase_returns_true(self):
        self.assertTrue(has_unique_chars(ascii_uppercase))

    def test_case_sensitive_word_returns_false(self):
        self.assertFalse(has_unique_chars("Songs"))

    def test_invalid_input_type_raises_error(self):
        # with dictionary
        with self.assertRaises(TypeError):
            has_unique_chars({})

        # with int input
        with self.assertRaises(TypeError):
            has_unique_chars(6)


if __name__ == '__main__':
    unittest.main()
