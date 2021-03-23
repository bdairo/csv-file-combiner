import argparse
import sys
from file_combiner import FileCombiner


def main():
    args = parse_args(sys.argv[1:])
    csv_combiner = FileCombiner(args)
    csv_combiner.combine_files()


def parse_args(args):
    # Create the parser
    parser = argparse.ArgumentParser(description='combine csv files')
    # Add arguments to parser
    parser.add_argument('files', type=argparse.FileType('r'), nargs='+',
                        help='paths of files to be combined')
    args = parser.parse_args(args)
    file_paths = []
    for file in args.files:
        file_paths.append(file.name)
    return file_paths


if __name__ == "__main__":
    main()
