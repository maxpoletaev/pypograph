from pypograph import Typograph, typo, rules
import unittest


class TestTypograph(unittest.TestCase):
    def test_typo(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'
        result = typo(text)

        self.assertEqual(result, expect)

    def test_rules_list(self):
        rules_list = [rules.NbspRule, rules.MdashRule]
        typograph = Typograph(rules_list)

        text = 'ab abc - abc'
        expect = 'ab&nbsp;abc —&nbsp;abc'
        result = typograph.typo(text)

        self.assertEqual(result, expect)
