#!/usr/bin/python
#
# Zadanie S1
# Jakub Sokolowski
# 15.06.2018 11:15 TP
#

import subprocess
import sys

def get_output_arr():
    output_str = subprocess.run(['netstat', '-tulpn'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    arr = []
    for line in output_str.split('\n'):
        arr.append(line.split())
    return arr[2:-1]



def get_all_ports(low, high):
    output = get_output_arr()
    result = []
    for entry in output:
        port = entry[3].split(':')[-1]
        if low < int(port) < high:
            print(entry[3])
            result.append(entry[3])
    return result


def get_listening_ports(low, high):
    output = get_output_arr()
    result = []
    for entry in output:
        port = int(entry[3].split(':')[-1])
        if low < port < high and entry[5] == "LISTEN":
            result.append(port)
    return result


def get_local_ports(low, high):
    output = get_output_arr()
    result = []
    for entry in output:
        adress = entry[3].split(':')
        if entry[5] == "LISTEN" and low < int(adress[-1]) < high:
            result.append(entry[3])
    return result


def main():
    low = int(sys.argv[1])
    high = int(sys.argv[2])
    print(low, high)
    for port in get_local_ports(low,  high):
        print(port)
    for lst_port in get_listening_ports(low, high):
        print(lst_port)


if __name__ == "__main__":
    main()