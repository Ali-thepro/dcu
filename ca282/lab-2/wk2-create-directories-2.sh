#!/bin/sh

n="$1"
i=1
while [ "$i" -le "$n" ]
do
    fileName=$(printf "dir.%06d\n" "$i")
    mkdir "$fileName"
    i=$((i+=1))
done
