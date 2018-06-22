#!/usr/bin/python
#
# Zadanie R2
# Jakub Sokolowski
# 08.06.2018 11:15 TP
#

import re
import subprocess


def valid_temp(temp: float):
    return 20.0 < temp < 80.0


def main():
    result = subprocess.run(['sensors'], stdout=subprocess.PIPE)
    pattern = re.compile("(\+)(\d{1,4}.\d)*(°)(C)")
    # Find matches to replace
    output_str = result.stdout.decode('utf-8')
    matches = []
    matches += re.finditer(pattern, output_str)
    for match in matches:
        if valid_temp(float(match.group(2))):
            print(match.group())


if __name__ == "__main__":
    main()