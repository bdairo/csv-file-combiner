import csv
import os
import sys


class FileCombiner:
    def __init__(self, args):
        self.file_paths = args
        self.is_header_set = False

    def add_new_column(self, row, column):
        row.append(column)

    def combine_files(self):
        # create a new stdout object
        combined = csv.writer(sys.stdout)

        # loop through array of file paths, set the names to a variable so we can use it later
        for file in self.file_paths:
            with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                header = next(csv_reader)
                if self.is_header_set is False:
                    self.add_new_column(header, 'filename')
                    combined.writerow(header)
                    self.is_header_set = True
                for row in csv_reader:
                    filename = os.path.basename(file) # add the name of the file to the last row
                    self.add_new_column(row, filename)
                    combined.writerow(row)

