#!/bin/bash
#
# Zadanie 85
# Jakub Sokołowski
# 06.04.2018 11:15 TP

FILE=$1
echo `awk '
BEGIN{i=0; nb_words=0; chars=0}
{
  chars+=length($0);
  nb_words+=NF;
  i++;
}
END{printf "Chars: " chars " Words: " nb_words  " Lines: " i }' $FILE`
