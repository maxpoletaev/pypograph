from pypograph import typograph
import unittest


class TestTypograph(unittest.TestCase):
    def test_typo(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'
        result = typograph.typo(text)

        self.assertEqual(result, expect)
