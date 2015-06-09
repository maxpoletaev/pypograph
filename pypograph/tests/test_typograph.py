from pypograph import Typograph, typo, rules
import unittest


class TestTypograph(unittest.TestCase):
    def test_typo(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'
        result = typo(text)

        self.assertEqual(result, expect)

    def test_rules_list(self):
        rules_list = [
            rules.NbspRule,
            rules.DashRule(),
            ('pypograph.rules.QuoteRule', {'quotes': '**'}),
        ]
        typograph = Typograph(rules_list)

        text = 'ab abc - abcdef "abc"'
        expect = 'ab&nbsp;abc —&nbsp;abcdef *abc*'
        result = typograph.typo(text)

        self.assertEqual(result, expect)
