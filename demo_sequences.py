#!/usr/bin/python
"""
Script to try out a few implementations of a specified sequence.
"""

import argparse
import sequences


def report(*sequences):
    """
    prints each sequence's contents along with its class name
    """
    for sequence in sequences:
        print(type(sequence).__name__, '--- \t' + str(sequence))


def parseSequence(function_name, args):
    """
    maps builtin function to each element in list and returns (reusable) list
    """
    return list(map(getattr(__builtins__, function_name), args))


def main():
    ap = argparse.ArgumentParser(description='Try out some operations on different sequence classes.')
    ap.add_argument('--type', '-t', choices=['int','str', 'float'], 
                    default='str', help='the type of the sequence elements, defaults to string')
    ap.add_argument('sequence', nargs='+')
    args = ap.parse_args()
    args.sequence = parseSequence(args.type, args.sequence)

    print('\nDemonstrating sequences with splay trees, lists, and typed lists under the hood')
    splay = sequences.SplaySequence()
    liszt = sequences.ListSequence()
    tlist = sequences.TypedListSequence()

    print('\nAdding each element in order:')
    for element in args.sequence:
        splay.add(element)
        liszt.add(element)
        tlist.add(element)
        report(splay, liszt, tlist)

    print('\nRemoving every other element:')
    for i, element in enumerate(args.sequence):
        if i % 2 == 1:
            splay.remove(element)
            liszt.remove(element)
            tlist.remove(element)
            report(splay, liszt, tlist)

    print('\nWhat remains?')
    for element in args.sequence:
        print(element, end=': ')
        print(all(((lambda x: element in x)(implementation)) 
                  for implementation in [splay, liszt, tlist])) 


if __name__ == "__main__":
    main()
