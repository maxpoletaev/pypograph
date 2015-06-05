from pypograph import utils
from unittest import TestCase


class TestUtils(TestCase):
    def test_pack_html(self):
        html = '<div>Hello world!</div>'
        expected = '[[PGRpdj4=]]Hello world![[PC9kaXY+]]'

        print()
        print(utils.unpack_html(html))

        self.assertEqual(utils.pack_html(html), expected)
