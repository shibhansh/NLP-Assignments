#!/bin/bash

# preporcessing
# 1. removing everything before first [ except '.'
# 2. removing everything between ] & [
# 3. removing ]
# 4. removing '+', '/' and '['
# 5. removing everything in line with ? except '.'

#NOW CONCATENATE

/usr/local/bin/english-analyze.sh xerox 53302.txt | sed "s/^[^.\[]*\[//g" | sed "s/\].*\[/ /g" | sed "s/\]//g" | sed "s/[+\/\[]/ /g" | sed "s/^[^.?]*?//g" | awk 'BEGIN { RS = "" ; OFS = " "} {$1 = $1; print}'  > temp.txt
