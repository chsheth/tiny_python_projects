#!/c/Users/csheth/AppData/Local/Microsoft/WindowsApps/python3


"""
Author:  CS
Purpose: Say hello
"""

import argparse


def get_args():
    """ Gets args """
    parser = argparse.ArgumentParser(description='Say hello')
    # parser.add_argument('name', help='Name to greet')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """ Main function """
    args=get_args()
    print("Hello, " + args.name + "!")


if __name__ == main():
    main()
