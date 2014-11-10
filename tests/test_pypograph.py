from pypograph import pypograph
import unittest


class TestPypograph(unittest.TestCase):

    def test_typo(self):
        text = '\t\tab abcd abcde a\tabcd\t\t'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'
        result = pypograph.typo(text)

        self.assertEqual(result, expect)
