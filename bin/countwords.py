"""
Count the occurences of all words in a text and output them in CSV file format.
"""

import argparse
import string
from collections import Counter

import utilities as util

# def collection_to_csv(collection, num=None):
#     """Write collection of items and counts in csv format."""
#     collection = collection.most_common()
#     if num is None:
#         num = len(collection)
#     writer = csv.writer(sys.stdout)
#     writer.writerows(collection[0:num])

# def update_counts(reader, word_counts):
#     """Update word counts with data form another reader/file."""
#     for word, count in csv.reader(reader):
#         word_counts[word] += int(count)

def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)
    return word_counts

def main(args):
    """Run the command line program"""
    word_count = count_words(args.infile)
    util.collection_to_csv(word_count, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default='-', help='Input file name')
    parser.add_argument('-n', '--num', type=int, default=None, help='Output n most frequent words')
    arg = parser.parse_args()
    main(arg)
