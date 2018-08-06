#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-05

Find Patterns Forming Clumps in a String

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval
of Genome of length L in which Pattern appears at least t times. For example, TGCA forms a (25,3)-clump in the following
Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.

Clump Finding Problem
Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.

Sample Dataset
CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4
Sample Output
CGACA GAAGA AATGT

Execute like:
python src/ba1e.py data/ba1e.txt output/ba1e.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput
from collections import deque


argv = list(sys.argv)

input_genome = ""
input_k = 0  # size of pattern
input_l = 0  # length of interval within genome
input_t = 0  # number of occurrences of kmer

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if " " in line:
            vals = line.split(" ")
            if len(vals) == 3:
                input_k = int(vals[0])
                input_l = int(vals[1])
                input_t = int(vals[2])
        else:
            input_genome += line.replace('\n', '')


def find_clumps(genome, k, l, t):
    """
    Return list of all distinct k-mers forming (L, t)-clumps in Genome, which is a pattern of size k that appears at
    least t times in an interval of length L in Genome
    :param genome: DNA string
    :type genome: str
    :param k: k-mer pattern size
    :type k: int
    :param l: length of interval within genome
    :type l: int
    :param t: minimum number of occurrences of k-mer pattern in genome
    :type t: int
    :return: list of (L, t)-clumps of size k in genome
    :rtype: list[str]
    """
    clumps = set()
    for i in range(0, len(genome) - l):                 # iterate over all intervals of length l in genome
        interval_deque = deque(genome[i:i+l])           # create interval of length l (substring of genome)
        kmer_occurrence_map = dict()
        kmer_buffer = ""
        for j in range(0, k):                           # build initial k-mer buffer from first k characters
            kmer_buffer += interval_deque.popleft()
        kmer_occurrence_map[kmer_buffer] = 1            # initialize number of occurrences to 1

        for base in interval_deque:                     # iterate over nucleobases left in interval deque
            kmer_buffer = kmer_buffer[1:] + base
            if kmer_buffer in kmer_occurrence_map:
                kmer_occurrence_map[kmer_buffer] += 1   # increment number of occurrences
            else:
                kmer_occurrence_map[kmer_buffer] = 1    # initialize number of occurrences to 1

        # find all (L, t)-clumps from current k-mer occurrence map and add to clump set
        for key, value in kmer_occurrence_map.items():
            if value >= t:
                clumps.add(key)

    return clumps


output_clumps = find_clumps(input_genome, input_k, input_l, input_t)

output_string = " ".join(output_clumps)

print("The following are the ({}, {})-clumps of size {} in genome \"{}\":\n{}".format(input_l, input_t, input_k,
                                                                                      input_genome, output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
