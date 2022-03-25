#!/c/Users/csheth/AppData/Local/Microsoft/WindowsApps/python3

# usr/bin/env/python3


"""
Author  :
Date    :
Purpose :
"""

import os
import argparse



def get_args():
    """ Get args """
    parser = argparse.ArgumentParser(description = 'Substitute all the vowels in a given text with a \
                                                    single vowel (default "a")',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        help='Enter input source: text or file',
                        metavar='input text',
                        type=str,
                        )

    parser.add_argument('-v',
                        '--vowel',
                        help='Enter vowel',
                        default='a',
                        metavar='Vowel',
                        )

    return parser.parse_args()

def main():
    args = get_args()

    text_args=args.text
    vowel_args=args.vowel

    if vowel_args in 'aeiouAEIOU':
        if os.path.isfile(text_args):
            with open(text_args, 'rt') as f:
                s = f.read().rstrip()
        else:
            s = text_args
        
        mytable = str.maketrans("aeiouAEIOU", vowel_args * 5 + vowel_args.upper() * 5)
        new_s = s.translate(mytable)
        print(new_s)
    else:    
        print(f'Please enter a valid vowel')

    

if __name__ =="__main__":
    main()