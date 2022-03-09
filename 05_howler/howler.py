#!/usr/bin/env python3


'''
Author  : Anon
Date    : 3/9/22
Purpose : Howler program
'''


import os
import argparse
import sys

from pytest import param


#-----
def get_args():
    ''' Get arguments '''
    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('text',
                        #nargs='+',
                        metavar='STR',
                        help='Input the text')

    parser.add_argument('-o',
                        '--out',
                        help='A readable file',
                        metavar='file',
                        default='')
                        
    return parser.parse_args()
    

#------
def main():
    ''' Main function '''
    args = get_args()
    
    if os.path.isfile(args.text):
        y = open(args.text).read().rstrip()
    else:
        y = args.text

    if args.out:
        print(y.upper(), file=open(args.out, 'wt'))
    else:
        print(y.upper())




#------
if __name__ == '__main__':
    main()