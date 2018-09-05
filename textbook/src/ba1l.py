#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-10

Implement PatternToNumber

Implement PatternToNumber
Convert a DNA string to a number.

Given: A DNA string Pattern.

Return: PatternToNumber(Pattern).

Sample Dataset
AGT
Sample Output
11

Input
CTTCTCACGTACAACAAAATC
Output
2161555804173


Execute like:
python3 src/ba1l.py data/ba1l.txt output/ba1l.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput

if __name__ == '__main__':
    from lib.bio_util import BioUtil
else:
    from .lib.bio_util import BioUtil

argv = list(sys.argv)

input_pattern = ""

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        input_pattern += line.replace('\n', '')


output_string = str(BioUtil.pattern_to_number(input_pattern))

print("The number representation of pattern \"{}\" is {}".format(input_pattern, output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
