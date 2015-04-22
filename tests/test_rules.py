from unittest import TestCase
from pypograph import rules


class NbspRuleTest(TestCase):
    def setUp(self):
        self.rule = rules.NbspRule()

    def test_process(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class MnemoRuleTest(TestCase):
    def test_process_mtu(self):
        rule = rules.MnemoRule({'mnemo_mode': 'html_to_utf8'})
        text = '&copy; &reg; &trade;'
        expect = '© ® ™'

        result = rule.process(text)
        self.assertEqual(result, expect)

    def test_process_utm(self):
        rule = rules.MnemoRule({'mnemo_mode': 'utf8_to_html'})
        text = '© ® ™'
        expect = '&copy; &reg; &trade;'

        result = rule.process(text)
        self.assertEqual(result, expect)

    def test_process_alias(self):
        rule = rules.MnemoRule({'mnemo_expand_alias': True})
        text = '(C) (R) (TM)'
        expect = '© ® ™'

        result = rule.process(text)
        self.assertEqual(result, expect)


class QuoteRuleTest(TestCase):
    def setUp(self):
        self.rule = rules.QuoteRule()

    def test_process(self):
        text = 'Lorem ipsum dolor sit amet, "consectetur adipiscing" elit.'
        expect = 'Lorem ipsum dolor sit amet, «consectetur adipiscing» elit.'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class TabRuleTest(TestCase):
    def setUp(self):
        self.rule = rules.TabRule()

    def test_process(self):
        text = "\t\tLorem ipsum dolor sit amet, consectetur adipiscing elit.\t\t\t\t"
        expect = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class OneSpaceRuleTets(TestCase):
    def setUp(self):
        self.rule = rules.OneSpaceRule()

    def test_process(self):
        text = 'Lorem  ipsum dolor   sit amet'
        expect = 'Lorem ipsum dolor sit amet'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class MdashRule(TestCase):
    def setUp(self):
        self.rule = rules.MdashRule()

    def test_process(self):
        text = '- Lorem ipsum dolor sit - amet'
        expect = '— Lorem ipsum dolor sit — amet'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    import unittest
    unittest.main()
