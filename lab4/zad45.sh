#!/bin/bash
#
# Zadanie 45
# Jakub Sokołowski
# 23.03.2018 11:15 TP
#
# Dla każdego plku w danym folderze wyświetla właściciela, grupę i uprawnienia
# jeśli ten plik nie należy do użytkownika 
DIR=$1
USER=$(whoami)
# Change to !
for FILE in `find $1 ! -user $USER`;
do
  OWNER=`stat -c %U $FILE`
  GROUP=`stat -c %G $FILE`
  PERMS=`stat -c %a $FILE`
  echo "Path: $FILE User: $OWNER, Group: $GROUP, Permissions: $PERMS"
done
