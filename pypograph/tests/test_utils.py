from pypograph import utils
from unittest import TestCase


class TestUtils(TestCase):
    def test_pack_html(self):
        html = '<div>Hello world!</div>'
        expected = '[[PGRpdj4=]]Hello world![[PC9kaXY+]]'
        self.assertEqual(utils.pack_html(html), expected)

    def test_unpack_html(self):
        html = '[[PGRpdj4=]]Hello world![[PC9kaXY+]]'
        expected = '<div>Hello world!</div>'
        self.assertEqual(utils.unpack_html(html), expected)
