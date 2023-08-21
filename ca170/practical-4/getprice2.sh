#!/bin/bash

url="https://bigcharts.marketwatch.com/historical/default.asp?symb=$1&closeDate=$3%2F$2%2F$4"

wget -q -0 - "$url" | tr -d "\015" | tr "\n" " " | sed "s|^.*Closing Price:</th>||g" | sed "s|</td>.*|\n|g" | sed "s|  *<td>||g"


#wget -q -O - "$url" | tr -d '\r' | tr -d '\n'|tr -d '\t\n\r' | sed -e 's/.*Closing Price:<\/th>//'|sed -e 's/<\/td>.*$/\n/g'|sed -e 's/[^0-9.,]*//g'
