#!/bin/sh

uniq -d | head -1

# while read line;
# do
#     if [ "$last" = "$line" ]; then
#         echo "$line"
#         break
#     fi
#     last="$line"
# done
