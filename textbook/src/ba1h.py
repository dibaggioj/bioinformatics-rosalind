#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-07

Find All Approximate Occurrences of a Pattern in a String

We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.

Approximate Pattern Matching Problem
Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

Sample Dataset
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3

Sample Output
6 7 26 27 78

Execute like:
python src/ba1h.py data/ba1h.txt output/ba1h.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput
from lib.bio_util import BioUtil


argv = list(sys.argv)

input_pattern = None
input_text = None
input_mismatches = -1

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if input_pattern is None:
            input_pattern = line.replace('\n', '')
        elif input_text is None:
            input_text = line.replace('\n', '')
        elif input_mismatches == -1:
            input_mismatches = int(line.replace('\n', ''))


def find_approximate_occurrences(pattern, text, d):
    """
    Find all starting positions where pattern appears as a substring of text with at most d mismatches.
    :param pattern:
    :type pattern: str
    :param text:
    :type text: str
    :param d:
    :type d: int
    :return: list of all starting positions where pattern appears as a substring of text with at most d mismatches.
    :rtype: list[int]
    """
    k = len(pattern)
    buffer = text[0:k]
    text = text[k:]
    i = 0
    indices = []
    if BioUtil.hamming_distance(buffer, pattern) <= d:
        indices.append(i)
    for c in text:
        i += 1
        buffer = buffer[1:k] + c
        if BioUtil.hamming_distance(buffer, pattern) <= d:
            indices.append(i)
    return indices


approximate_occurrences = find_approximate_occurrences(input_pattern, input_text, input_mismatches)

print(approximate_occurrences)

output_string = " ".join(str(i) for i in approximate_occurrences)

print("The indices of where \"{}\" appears as a substring of \"{}\" with at most {} mismatches are:\n{}".format(
    input_pattern, input_text, str(input_mismatches), output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
