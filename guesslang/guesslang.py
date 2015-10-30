#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from langdetect import detect

def main():
    """
    guesslang entry point
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
            'text',
            help='the text for which to guess the language')

    args = parser.parse_args()

    print language(args.text)
    return

def language(txt):
    """ returns the language of the txt """

    lang = None
    try:
        lang = detect(txt)
    except:
        pass

    return lang


if __name__ == '__main__':
    main()
