#!/bin/bash
python concatenate.py

perl -pi -e 's/[[:^ascii:]]//g' train_neg.txt
perl -pi -e 's/[[:^ascii:]]//g' train_pos.txt
perl -pi -e 's/[[:^ascii:]]//g' test_neg.txt
perl -pi -e 's/[[:^ascii:]]//g' test_pos.txt

sed -i -e 's/\(.*\)/\L\1/' train_neg.txt
sed -i -e 's/\(.*\)/\L\1/' train_pos.txt
sed -i -e 's/\(.*\)/\L\1/' test_neg.txt
sed -i -e 's/\(.*\)/\L\1/' test_pos.txt