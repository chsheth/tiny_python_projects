#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@dewill-061928>
Date   : 2022-03-01
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    parser.add_argument('-s', '--side',
                        metavar='side',
                        default = 'larboard',
                        help='Which side')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word_arg = args.word
    side_arg = args.side
    if word_arg[0].lower() in ['a','e','i','o','u']:
        x = 'an'
    else:
        x = 'a'
    print(f'Ahoy, Captain, {x} {word_arg} off the {side_arg} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
