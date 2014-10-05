from pypograph import processors
import unittest


class NbspProcessorTest(unittest.TestCase):

    def setUp(self):
        self.processor = processors.NbspProcessor()

    def test_process(self):
        text = 'ab abcd abcde a abcd'
        expect = 'ab&nbsp;abcd abcde a&nbsp;abcd'
        result = self.processor.process(text)

        self.assertEqual(result, expect)


class MnemoProcessorTest(unittest.TestCase):

    def test_process_mtu(self):
        processor = processors.MnemoProcessor({
            'mnemo_mode': 'html_to_utf8'
        })

        text = 'ab &mdash; cde &copy;'
        expect = 'ab — cde ©'

        result = processor.process(text)
        self.assertEqual(result, expect)

    def test_process_utm(self):
        processor = processors.MnemoProcessor({
            'mnemo_mode': 'utf8_to_html'
        })

        text = 'ab — cde ©'
        expect = 'ab &mdash; cde &copy;'

        result = processor.process(text)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
