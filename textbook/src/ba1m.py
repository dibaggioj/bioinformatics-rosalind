#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-09-04

Implement NumberToPattern

Implement NumberToPattern
Convert an integer to its corresponding DNA string.

Given: Integers index and k.

Return: NumberToPattern(index, k).

Sample Dataset
45
4
Sample Output
AGTC

Extra Dataset
Input
5353
7
Output
CCATGGC

Execute like:
python3 src/ba1m.py data/ba1m.txt output/ba1m.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput

if __name__ == '__main__':
    from lib.bio_util import BioUtil
else:
    from .lib.bio_util import BioUtil

argv = list(sys.argv)

input_number = -1
input_k = -1

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if input_number == -1:
            input_number = int(line.replace('\n', ''))
        elif input_k == -1:
            input_k = int(line.replace('\n', ''))


output_string = BioUtil.number_to_pattern(input_number, input_k)

print("The {}-mer pattern for number {} is \"{}\"".format(str(input_k), str(input_number), output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()

