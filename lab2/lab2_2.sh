#!/bin/sh

IN=$1

INDEX=1

echo $1

for FILE in `ls -S $1`;
do
    #echo $FILE
    if [ -x "$FILE" ]; then
        echo "$FILE"
       # mv "$FILE" "$FILE.$INDEX"
        INDEX=$((INDEX+1)) 
    fi
done
