"""Brief description of what the file does."""

import argparse
import glob


def main(args):
    """Runs the program"""
    fnames = args.dir + '/*.' + args.suffix
    print(glob.glob(fnames))


if __name__ == '__main__':
    USAGE = 'List the files in a given directory with a given suffix.'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type=str, help='Directory')
    parser.add_argument('suffix', type=str, help='File suffix (e.g., py, sh, md)')
    args = parser.parse_args()
    main(args)