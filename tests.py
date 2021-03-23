import importlib
import sys
import unittest
from io import StringIO
from unittest.mock import patch

import file_combiner

csv_combiner = importlib.import_module("csv-combiner")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.file_paths = csv_combiner.parse_args(['file1.csv', 'file2.csv'])
        self.combined = file_combiner.FileCombiner(self.file_paths)

    def test_parser(self):
        actual_file_paths = ['file1.csv', 'file2.csv']
        self.assertCountEqual(self.file_paths, actual_file_paths)

    def test_add_new_column(self):
        row = ['email_hash', 'category']
        self.combined.add_new_column(row, 'filename')
        expected_row = ['email_hash', 'category', 'filename']
        self.assertEqual(row, expected_row)

    def test_output(self):
        out = StringIO
        sys.stdout = out
        output = out.getvalue(self.combined.combine_files())
        self.assertEqual(output,
                         'email_hash,category,filename\n' + 'b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Satchels,filename\n' +
                         'b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Blouses,filename\n' + 'b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Kitchen Cleaner,filename')


if __name__ == '__main__':
    unittest.main()

# python -m unittest tests.py
