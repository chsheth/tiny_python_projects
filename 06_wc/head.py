#!/usr/bin/env python3


"""
Author  : CS
Date    : 3/14/22
PUrpose : Emulate head
"""


import argparse
import os
import sys


def get_args():
    """ Get args """
    parser = argparse.ArgumentParser(description='Head program',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        help = 'Num. of lines',
                        metavar='lines',
                        type = int,
                        default=10)

    parser.add_argument('file',
                        help = 'Input file(s)',
                        nargs='+', #one or more
                        metavar='FILE',
                        type = argparse.FileType('rt'), #need a readable file
                        default=[sys.stdin])

    return parser.parse_args()



def main():
    """ Main function """
    args=get_args()
    file_args = args.file
    print(args.num)
    if args.num:
        file_num = args.num
    else:
        file_num=10

    for fh in file_args:
        num_lines = 0
        print(f"{fh.name}")
        for line in fh:
            y = fh.readline()
            print(y, end='')
            num_lines += 1
            if num_lines == file_num:
                print()
                break 
    


if __name__ == '__main__':
    main()


"""
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
"""