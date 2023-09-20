#!/bin/sh

while read line
do
    test -f "$line" || { echo "$line"; exit 0;}
done

# while read line
# do
#     test -f "$line" || { echo "$line"; break;}
# done
