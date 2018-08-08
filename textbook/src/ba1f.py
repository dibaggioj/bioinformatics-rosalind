#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-07

Find a Position in a Genome Minimizing the Skew

Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

Minimum Skew Problem
Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

Sample Dataset
CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG
Sample Output
53 97

Execute like:
python src/ba1f.py data/ba1f.txt output/ba1f.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput


argv = list(sys.argv)

input_genome = ""

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        input_genome += line.replace('\n', '')


def find_skew(genome):
    """
    Return list of all skew values across the genome
    :param genome: DNA string
    :type genome: str
    :return: list of skew values across the genome
    :rtype: list[int]
    """
    skew = list([0])  # initialize list with 0 skew at beginning
    current_skew = 0
    for c in genome:
        if c == 'C':
            current_skew -= 1
        elif c == 'G':
            current_skew += 1
        skew.append(current_skew)
    return skew


def minimize_skew(genome):
    """
    Return all integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
    :param genome:
    :type genome: str
    :return: list of integers minimizing the skew of genome
    :rtype: list[int]
    """
    skew = find_skew(genome)
    minima = list()
    minimum = min(skew)
    current_position = 0
    for s in skew:
        if s == minimum:
            minima.append(current_position)
        current_position += 1
    return minima


def minimize_skew_2(genome):
    """
    Return all integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
    :param genome:
    :type genome: str
    :return: list of integers minimizing the skew of genome
    :rtype: list[int]
    """
    current_position = 0
    current_skew = 0
    minimum_skew = current_skew
    minima = list()
    for c in genome:
        current_position += 1
        if c == 'C':
            current_skew -= 1
        elif c == 'G':
            current_skew += 1
        if current_skew < minimum_skew:
            minimum_skew = current_skew
            minima = list([current_position])
        elif current_skew == minimum_skew:
            minima.append(current_position)
    return minima


output_minima = minimize_skew(input_genome)

output_string = " ".join(str(i) for i in output_minima)

print("The positions {} minimize the skew in genome:\n\"{}\"".format(output_string, input_genome))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
