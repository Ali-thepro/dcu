#!/bin/sh

n="$1"
i=0
while [ "$i" -lt "$n" ]
do
    fileName=$((i+=1))
    mkdir "dir.$fileName"
done


# i=1
# while [ $i -le $1 ];
# do
#     mkdir "dir.$i"
#     i=$((i+1))
# done



# n="$1"
# seq -f "dir.%.0f" $n | xargs mkdir

# n="$1"
# mkdir $(seq -f "dir.%.0f" $n)

# for n in $(seq $1)
# do
#     mkdir "dir.$n"
# done


# seq "$1" |
# while read n
# do
#     mkdir "dir.$n"
# done
