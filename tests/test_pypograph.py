from pypograph import pypograph
import unittest


class TestPypograph(unittest.TestCase):

    def test_typo(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'
        result = pypograph.typo(text)

        self.assertEqual(result, expect)
