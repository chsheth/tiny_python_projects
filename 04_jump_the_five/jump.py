#!/usr/bin/env python3


'''
Author  : Amon
Date    : 2022-03-08
Purpose : Write a jumper code that Jumps the 5
'''


import argparse


#---------------------
def get_args():
    '''Gets the arguments'''

    parser = argparse.ArgumentParser(
        description = "Jump the 5",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter )

    parser.add_argument('text',
                        metavar = 'str',
                        help = 'Inputs the text')

    return parser.parse_args()


#-------------------------    
def main():
    '''Main function'''
    args = get_args()
    text_args = args.text

    jumper = {'1':'9','2':'8','3':'7','4':'6','5':'0',
                '6':'4','7':'3','8':'2','9':'1','0':'5'}
    
    for char in text_args:
        if char in jumper:
            print(jumper[char], end='')
        else:
            print(char, end='')
    print()

#-------------------------
if __name__ == '__main__':
    main()