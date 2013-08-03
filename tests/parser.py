import unittest

from robot import parser


class ParserTestCase(unittest.TestCase):

    def test_limits(self):
        limit = parser.limit('12 15')
        self.assertEqual(limit, (12, 15))
        self.assertEqual(len(limit), 2)

        with self.assertRaises(ValueError):
            parser.limit('')
            parser.limit('12')
            parser.limit('12 13 15')
            parser.limit('RLW')

    def test_initial_position(self):
        position = parser.initial_position('10 12 N')
        self.assertEqual(position, ((10, 12), 'N'))
        with self.assertRaises(ValueError):
            parser.initial_position('')
            parser.initial_position('12')
            parser.initial_position('12 13 15')
            parser.initial_position('12 S 11')
            parser.initial_position('RLW')

if __name__ == "__main__":
    unittest.main()
