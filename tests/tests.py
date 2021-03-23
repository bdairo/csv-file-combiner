import csv
import importlib
import sys
import unittest
import file_combiner
csv_combiner = importlib.import_module("csv-combiner")


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_paths = csv_combiner.parse_args(['file1.csv', 'file2.csv'])
        self.combined = file_combiner.FileCombiner(self.file_paths)
        original = sys.stdout
        with open('actual.csv', 'w') as file:
            sys.stdout = file
            self.combined.combine_files()
            sys.stdout = original

    def test_combine_files(self):
        with open('actual.csv') as actual, open('expected.csv') as expected:
            actual_file = csv.reader(actual)
            expected_file = csv.reader(expected)
            for file1_line in actual_file:
                file2_line = next(expected_file)
                self.assertEqual(file1_line, file2_line)

    def test_parse_args(self):
        actual_file_paths = ['file1.csv', 'file2.csv']
        self.assertCountEqual(self.file_paths, actual_file_paths)

    def test_add_new_column(self):
        row = ['email_hash', 'category']
        self.combined.add_new_column(row, 'filename')
        expected_row = ['email_hash', 'category', 'filename']
        self.assertEqual(row, expected_row)


if __name__ == '__main__':
    unittest.main()

# python -m unittest tests.py
