#!/bin/sh

n="$1"
i=1
while [ "$i" -le "$n" ]
do
    fileName=$(printf "dir.%06d\n" "$i")
    mkdir "$fileName"
    i=$((i+=1))
done

# n="$1"
# i=1
# while [ "$i" -le "$n" ]
# do
#     fileName=$(printf "%06d\n" "$i")
#     mkdir "dir.$fileName"
#     i=$((i+=1))
# done



# n="$1"
# seq -f "dir.%06.0f" $n | xargs mkdir