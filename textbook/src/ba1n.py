#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-10

The d-neighborhood Neighbors(Pattern, d) is the set of all k-mers whose Hamming distance from Pattern does not exceed d.

Generate the d-Neighborhood of a String
Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).

Sample Dataset
ACG
1
Sample Output
CCG
TCG
GCG
AAG
ATG
AGG
ACA
ACC
ACT
ACG

Execute like:
python3 src/ba1n.py data/ba1n.txt output/ba1n.txt

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
input_d = 0

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        text = line.replace('\n', '')
        try:
            val = int(text)
            input_d = val
        except ValueError:
            input_pattern += text


d_neighbors = BioUtil.neighbors(input_pattern, input_d)

output_string = "\n".join(d_neighbors)

print("The {}-neighborhood of pattern \"{}\" are:\n{}".format(input_d, input_pattern,output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
