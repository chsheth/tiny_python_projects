#!/usr/bin/env python3


"""
Author  : CS
Date    : 3/16/22
Purpose : Dictionary lookup
"""


import os
import argparse
import sys



def get_args():
    """ Get arguments """
    parser = argparse.ArgumentParser(description = 'Return the sentence corresponding to \
                                                 the alphabet ',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('char',
                        help='Enter character',
                        nargs='+',
                        metavar='Char',
                        )

    parser.add_argument('-f',
                        '--file',
                        help = 'Input file(s)',
                        metavar='FILE',
                        type = argparse.FileType('rt'),
                        default= 'gashlycrumb.txt',
                        )

    return parser.parse_args()




def main():
    """ Main function """
    args = get_args()

    char_arg = args.char
    file_arg = args.file

    d = {}                              # create an empty dictionary to output the statement
    for line in file_arg:
        """
        - we do not need to use 'open' because of the way the file argument is added in argparse
        - it can be thought that the file handle is created and opened in argparse option
        - so we can directly read the file; else we would need a 'with' or 'open' statement
        - this would create a file handle and then we use 'read'
        """
        d[line[0].upper()] = line[:-1]
        
    for char in char_arg:
        if char not in 'abcdefghijklmnopqrstuvwxy':
            print(f'I do not know "{char}".')
        else:
            y = d[char.upper()]
            print(y)


if __name__ == "__main__":
    main()