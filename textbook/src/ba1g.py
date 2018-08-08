#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-07

Compute the Hamming Distance Between Two Strings

We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two
mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is
denoted HammingDistance(p, q).

Hamming Distance Problem
Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.

Sample Dataset
GGGCCGTTGGT
GGACCGTTGAC

Sample Output
3

Execute like:
python src/ba1g.py data/ba1g.txt output/ba1g.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput
from collections import deque


argv = list(sys.argv)

input_dna_string_1 = ""
input_dna_string_2 = ""

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if len(input_dna_string_1) == 0:
            input_dna_string_1 += line.replace('\n', '')
        else:
            input_dna_string_2 += line.replace('\n', '')


def hamming_distance(p, q):
    """
    Return integer value representing the Hamming distance between DNA strings p and q
    :param p: DNA string 1
    :type p: str
    :param q: DNA string 2
    :type q: str
    :return: Hamming distance between DNA strings p and q
    :rtype: int
    """
    mismatches = 0
    p_bases = deque(p)
    q_bases = deque(q)

    while len(p_bases) > 0 and len(q_bases) > 0:
        if p_bases.popleft() != q_bases.popleft():
            mismatches += 1

    return mismatches


output_hamming_distance = hamming_distance(input_dna_string_1, input_dna_string_2)

print(output_hamming_distance)

output_string = str(output_hamming_distance)

print("The Hamming distance of DNA strings \"{}\" and \"{}\": is: {}".format(input_dna_string_1, input_dna_string_2,
                                                                             output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
