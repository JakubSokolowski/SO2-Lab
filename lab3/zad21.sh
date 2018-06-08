#!/bin/bash
#
# Zadanie 21
# Jakub Sokołowski
# 09.03.2018 11:15 TP
#
# Dla każdego pliku w danym folderze tworzy 
# łącze symboliczne, jeśli takie nie istnieje

#cd $1

IN=$1
OUT=$2
for FILE in $IN*;
do
    # Get the filename from path
    NAME=$(basename $FILE)
    echo $OUT$NAME
    if [ -L "$OUT$NAME" ]; then
        echo "$OUT$NAME symlink exists"
    else
        ln -s $FILE $2
    fi
done
