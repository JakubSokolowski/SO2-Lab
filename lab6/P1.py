#!/usr/bin/python

import sys
import os


def remove_non_ex(path: str):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            if os.path.isfile(file_path):
                if not os.access(file_path, os.X_OK):
                    print(file_path)
        except Exception as e:
            print(e)
    return


def main():
    remove_non_ex(sys.argv[1])
    # print command line arguments
    # for arg in sys.argv[1:]:
    #     print(arg)


if __name__ == "__main__":
    main()
