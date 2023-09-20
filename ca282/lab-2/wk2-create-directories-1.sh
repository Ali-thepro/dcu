#!/bin/sh

n="$1"
i=0
while [ "$i" -lt "$n" ]
do
    mkdir "dir."$((i+=1))
done


# i=1
# while [ $i -le $1 ];
# do
#     mkdir "dir.$i"
#     i=$((i+1))
# done
