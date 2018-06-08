#!/bin/bash
#
# Zadanie 93
# Jakub Sokołowski
# 06.04.2018 11:15 TP
#

WEBSITE=$1
#wget -r -A=.jpg,.png,.gif $1 > intex.htmlc

#wget -qO- $1 > index.html
for IMAGE in `grep -Eo '([a-z\-\_0-9\/\:\.]*\.(jpg|png|gif))' index.html`;
do
  wget -q $WEBSITE$IMAGE -P ./out
  #echo $WEBSITE$IMAGE
done

for CSS in `grep -Eo '([a-z\-\_0-9\/\:\.]*\.(css))' index.html`;
do
  for CSS_IMAGE in `wget -q0- $WEBSITE$CSS | grep -Eo '([a-z\-\_0-9\/\:\.]*\.(jpg|png|gif))'`
  do
  done
done
