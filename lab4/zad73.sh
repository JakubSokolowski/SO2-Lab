#!/bin/bash
#
# Zadanie 73
# Jakub Sokołowski
# 23.03.2018 11:15 TP
#
# a)
NUM=${1-10}
COUNT=`lsof | wc -l`
echo $COUNT
echo $NUM
# b), c)
lsof | grep REG | tr -s ' ' | cut  -d ' ' -f7,9 | sort -rn -t ' ' -k1 |  head -n $NUM
# d) niedokończone
for pid in `lsof | tr -s ' ' | cut -d ' ' -f2`;
 do
    COUNT=`ls /proc/$pid/fd/ | wc -l`
    echo $PID $COUNT
done
