#!/bin/sh

var1="$1"
var2="$2"
if [ "$var1" = "$var2" ]; then
    echo "the same"
else
    echo "different"
fi
