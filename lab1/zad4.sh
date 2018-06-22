#!/bin/bash
#
# Skrypt nr 4 z listy so_lab1 na zsk
# Jakub Sokołowski
# 09.03.2018 11:15 TP
#
# Numerowanie plików wykonywalnych w danym folderze
# według ich rozmiar

INDEX=1

for FILE in `ls $1 -S`;
do
    if [ -x "$1$FILE" ]; then
        echo "$FILE"
        mv "$1$FILE" "$1$FILE.$INDEX"
        INDEX=$((INDEX+1)) 
    fi
done
