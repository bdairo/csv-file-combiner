import argparse
import csv
import os
import sys


def main():
    file_paths = parse_args(sys.argv[1:])
    combine_files(file_paths)


def parse_args(args):
    # Create the parser
    parser = argparse.ArgumentParser(description='combine csv files')
    # Add arguments to parser
    parser.add_argument('files', type=argparse.FileType('r'), nargs='+',
                        help='paths of files to be combined')
    args = parser.parse_args()
    file_paths = []
    for file_path in args.files:
        file_paths.append(file_path.name)

    return file_paths


def combine_files(file_paths):
    # get arguments
    # create and open a csv where we will put all new files in
    combined = csv.writer(sys.stdout)
    # set header in combined csv file
    with open(file_paths[0], 'r') as first_file:
        reader = csv.reader(first_file, delimiter=',')
        header = next(reader)
        header.append('filename')
        combined.writerow(header)

    # loop through array of file paths, set the names to a variable so we can use it later
    for filename in file_paths:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)  # skip headers in files
            for row in csv_reader:
                # add all the content to the combined csv file
                sanitizefilename = os.path.basename(filename)
                row.append(sanitizefilename)
                combined.writerow(row)


if __name__ == "__main__":
    main()
