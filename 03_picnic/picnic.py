#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@dewill-061928>
Date   : 2022-03-07
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Items to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether the list should be sorted',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    #str_arg = args.arg
    flag_arg = args.sorted
    pos_arg = args.items

    l = len(pos_arg)
    if flag_arg:
        pos_arg.sort()

    if l == 1:
        print(f'You are bringing {pos_arg}.')
    elif l == 2:
        print(f'You are bringing {pos_arg[0]} and {pos_arg[1]}.')
    else:
        s1 = ', '.join(pos_arg[0:-1])
        s2 = pos_arg[-1]
        print(f'You are bringing {s1} and {s2}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
