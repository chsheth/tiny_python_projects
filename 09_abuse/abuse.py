#!/c/Users/csheth/AppData/Local/Microsoft/WindowsApps/python3


"""
Author  :
Purpose :
Date    :
"""

import argparse
import os
import random

def get_args():
    """ Arguments """
    parser = argparse.ArgumentParser(description = 'Create insults',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--number',
                        metavar='int',
                        help = 'Enter number of insults',
                        default = 3,
                        type = int
    )

    parser.add_argument('-a',
                        '--adjectives',
                        metavar ='int',
                        help='Enter number of adjectives',
                        type = int,
                        default=2,
    )

    parser.add_argument('-s',
                        '--seed',
                        metavar ='int',
                        type = int,
                        help='Random seed',
                        default=None,
    )

    args = parser.parse_args()
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    return args

def main():
    """ Main function """
    args = get_args()
    num = args.number
    adj = args.adjectives

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.split()

    random.seed(args.seed)

    for i in range(num):
        show_noun = []
        show_adj =[]
        show_noun = random.choice(nouns)
        show_adj = random.sample(adjectives, adj)
        sent = ', '.join(show_adj)
        print(f'You {sent} {show_noun}!')

if __name__ == "__main__":
    main()

