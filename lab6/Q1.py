#!/usr/bin/python

import sys
import os
import stat
import errno
from collections import defaultdict
from itertools import islice


# a)
def can_execute(directory, file):
    return len(sys.argv) == 3 and os.access(directory, os.W_OK) and os.access(file, os.R_OK)


def create_content_dict(file):
    files = defaultdict(list)
    with open(file) as f:
        file_iter = iter(f)
        last_line = ""
        for line in file_iter:
            line = line.rstrip()
            if str(line).isdigit():
                contents = list(islice(file_iter, int(line)))
                files[last_line] = contents
            else:
                last_line = line
                files[last_line] = []
    return files


def get_available_path(path):
    if not os.path.exists(path):
        return path
    filename, file_extension = os.path.splitext(path)
    i = 1
    new_filename = "{}_{}{}".format(filename, i, file_extension)
    while os.path.exists(new_filename):
        i += 1
        new_filename = "{}_{}{}".format(filename, i, file_extension)
    return new_filename


def create_file(path: str, content: list):
    # if file exists, add suffix
    path = get_available_path(path)
    # if the path does not exist, create the dirs
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(path, "w") as f:
        for line in content:
            f.write(line)


def create(directory, file):
    files = create_content_dict(file)
    for path, content in files.items():
        file_path = os.path.join(directory, path)
        print(file_path)
        create_file(file_path, content)


def main():
    # argv[1] - dir, argv[2] - list file
    if can_execute(sys.argv[1], sys.argv[2]):
        print("Can execute!")
        create(sys.argv[1], sys.argv[2])

    # print command line arguments
    # for arg in sys.argv[1:]:
    #     print(arg)


if __name__ == "__main__":
    main()
