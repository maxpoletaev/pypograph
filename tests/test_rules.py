from pypograph import rules
import unittest


class NbspRuleTest(unittest.TestCase):

    def setUp(self):
        self.rule = rules.NbspRule()

    def test_process(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'

        result = self.rule.process(text)
        self.assertEqual(result, expect)


class MnemoRuleTest(unittest.TestCase):

    def test_process_mtu(self):
        rule = rules.MnemoRule({
            'mnemo_mode': 'html_to_utf8'
        })

        text = 'ab &mdash; cde &copy;'
        expect = 'ab — cde ©'

        result = rule.process(text)
        self.assertEqual(result, expect)

    def test_process_utm(self):
        rule = rules.MnemoRule({
            'mnemo_mode': 'utf8_to_html'
        })

        text = 'ab — cde ©'
        expect = 'ab &mdash; cde &copy;'

        result = rule.process(text)
        self.assertEqual(result, expect)


class QuoteRuleTest(unittest.TestCase):

    def setUp(self):
        self.rule = rules.QuoteRule()

    def test_process(self):
        text = 'Lorem ipsum dolor sit amet, "consectetur adipiscing" elit.'
        expect = 'Lorem ipsum dolor sit amet, «consectetur adipiscing» elit.'

        result = self.rule.process(text)
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()
