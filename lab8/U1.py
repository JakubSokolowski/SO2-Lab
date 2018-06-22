#!/usr/bin/python
# coding=UTF8
# Zadanie U1
# Jakub Sokołowski
# 08.06.2018 11:15 TP
#
import re
import datetime
import os

def date_to_eu(filename):
    if not os.path.isfile(filename):
        print("file does not exist")
        return
    pattern = re.compile(r"(^\d{1,2})[\/|\.](\d{1,2})[\/|\.](\d{4})")
    for line in open(filename):
        for match in re.finditer(pattern, line):
                print(match.group())
    for line in open(filename):
        line = re.sub(r"(\d{1,2})[\/|\.](\d{1,2})[\/|\.](\d{4})",r"\2.\1.\3",line)
        print(line)
    return

def date_na(date_string):
    date_list = re.split(r"\/|\.",date_string)
    date_list[0], date_list[1] = date_list[1], date_list[0]
    return "/".join(date_list)


def celc_to_far(filename):
    pattern = re.compile(r"(\+)(\d{1,4}.\d)*(°)(C)")
    # Find matches to replace
    matches = []
    for line in open(filename):
        matches += re.finditer(pattern, line)

    whole_file = ""
    for line in open(filename):
        whole_file += re.sub(r"(\+)(\d{1,4}.\d)*(°)(C)" ,r"\1" + r"\2" +r"\3F",line)

    for match in matches:
        whole_file = whole_file.replace(match.group(2), str(to_far(match.group(2))))
    print(whole_file)
    return



def to_far(num):
    return 9.0/5.0 * float(num) + 32


def main():
  # date_to_eu("nowomow.txt")
   celc_to_far("sensors.txt")
   return

if __name__ == "__main__":
    main()
