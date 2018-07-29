#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-07-28

Find All Occurrences of a Pattern in a String

In this problem, we ask a simple question: how many times can one string occur as a substring of another? Recall from “Find the Most Frequent Words in a String” that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.

Pattern Matching Problem
Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.

Sample Dataset
ATAT
GATATATGCATATACTT
Sample Output
1 3 9

Execute like:
python src/ba1d.py data/ba1d.txt output/ba1d.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput


argv = list(sys.argv)

input_pattern = ""
input_genome = ""

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if len(input_pattern) == 0:
            input_pattern += line.replace('\n', '')
        else:
            input_genome += line.replace('\n', '')


def find_occurrences(genome, pattern):
    """
    Find the indices of all occurrences of pattern in genome
    :param genome: DNA substring
    :type genome: str
    :param pattern: DNA string
    :type pattern: str
    :return: list of indices of occurrences of pattern in genome
    :rtype: list[int]
    """
    k = len(pattern)
    buffer = genome[0:k]
    genome = genome[k:len(genome)]
    i = 0
    indices = []
    if buffer == pattern:
        indices.append(i)
    for c in genome:
        i += 1
        buffer = buffer[1:k] + c
        if buffer == pattern:
            indices.append(i)
    return indices


occurrences = find_occurrences(input_genome, input_pattern)

output_string = str.join(" ", [str(i) for i in occurrences])

print("The following are the occurrences of pattern \"{}\" in genome \"{}\":\n{}".format(input_pattern, input_genome,
                                                                                         output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
