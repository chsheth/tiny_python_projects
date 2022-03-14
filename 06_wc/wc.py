#!/usr/bin/env python3


"""
Author  : CS
Date    : 3/14/22
PUrpose : Emulate wc
"""


import argparse
import os
import sys


def get_args():
    """ Get args """
    parser = argparse.ArgumentParser(description='Word Count program',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help = 'Input file(s)',
                        nargs='*',
                        metavar='FILE',
                        type = argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()



def main():
    """ Main function """
    args=get_args()
    file_args = args.file 
    tot_lines, tot_words, tot_chars = 0, 0, 0
    for fh in file_args:
        num_lines, num_words, num_chars = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split()) 
            num_chars += len(line)
        print(f"{num_lines:8} {num_words:8} {num_chars:8} {fh.name}")
        tot_lines += num_lines
        tot_words += num_words
        tot_chars += num_chars
    print(f"{tot_lines:8} {tot_words:8} {tot_chars:8} total")

if __name__ == '__main__':
    main()