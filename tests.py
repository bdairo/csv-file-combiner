import unittest
import csv_combiner


class MyTestCase(unittest.TestCase):
    def test_parser(self):
        parser = csv_combiner.parse_args(['./fixtures/accessories.csv', './fixtures/clothing.csv'])
        self.assertTrue(parser.long)


if __name__ == '__main__':
    unittest.main()
