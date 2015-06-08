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
    def test_process(self):
        rule = rules.MnemoRule(expand_alias=True)
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


class OneSpaceRuleTets(TestCase):
    def setUp(self):
        self.rule = rules.OneSpaceRule()

    def test_process(self):
        text = 'Lorem  ipsum dolor   sit amet'
        expect = 'Lorem ipsum dolor sit amet'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class DashRule(TestCase):
    def setUp(self):
        self.rule = rules.DashRule()

    def test_process_text(self):
        text = '- Lorem ipsum -- dolor sit - amet'
        expect = '— Lorem ipsum — dolor sit — amet'

        result = self.rule.process(text)
        self.assertEqual(result, expect)

    def test_process_digts(self):
        text = 'Lorem ipsum 1994-2015'
        expect = 'Lorem ipsum 1994–2015'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class PunctuactionRuleTest(TestCase):
    def setUp(self):
        self.rule = rules.PunctuationRule()

    def test_process(self):
        text = 'Lorem ipsum , dolor,sit, amet !'
        expect = 'Lorem ipsum, dolor, sit, amet!'

        result = self.rule.process(text)
        self.assertEqual(result, expect)
