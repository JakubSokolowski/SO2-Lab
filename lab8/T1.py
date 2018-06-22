#!/usr/bin/python
#
# Zadanie T1
# Jakub Sokolowski
# 08.06.2018 11:15 TP
#

import re
import sys


def main():
    pattern = re.compile(r"(\+\d\d\D)?(\d{3})\D?(\d{3})\D?(\d{3})")
    for line in open(sys.argv[1]):
        for match in re.finditer(pattern, line):
            print(match.group())
    return


if __name__ == "__main__":
    main()