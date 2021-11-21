import argparse
import string
from collections import Counter

# import utilities as util


def count_puncs(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    # nfullstop = 0
    nfullstop = [word.count('.') for word in chunks]
    # print(sum(nfullstop))
    nqmark = [word.count('?') for word in chunks]
    nexpoint = [word.count('!') for word in chunks]
    punc_list = {'# of full stops': sum(nfullstop), '# of question marks': sum(nqmark), '# of exclamation points': sum(nexpoint)}
    # word_counts = Counter(word_list)
    return punc_list
def main(args):
    """Run the command line program"""
    punc_count = count_puncs(args.infile)
    print(punc_count)
    # util.collection_to_csv(word_count, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default='-', help='Input file name')
    parser.add_argument('-n', '--num', type=int, default=None, help='Output n most frequent words')
    arg = parser.parse_args()
    main(arg)