#!/bin/sh

set -e

for file in "$@";
do
    test -f "$file"
done


# for file in "$@";
# do
#     test -f "$file" || exit 1
# done
