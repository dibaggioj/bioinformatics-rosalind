#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-07-28

Find the Reverse Complement of a String

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a DNA string Pattern = p1…pn is the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

Reverse Complement Problem
Find the reverse complement of a DNA string.

Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT

Execute like:
python src/ba1c.py data/ba1c.txt output/ba1c.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput

COMPLEMENTARY_NUCLEOTIDE_MAP = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def complement(dna):
    """
    Return the complement of DNA string
    :param text: DNA string
    :type dna: str
    :return: complement of DNA string
    :rtype: str
    """
    dna_complement = [None]*len(dna)
    i = 0
    for nb in dna:
        if nb in COMPLEMENTARY_NUCLEOTIDE_MAP:
            dna_complement[i] = COMPLEMENTARY_NUCLEOTIDE_MAP[nb]
            i += 1
        else:
            raise ValueError("Invalid nucleotide base \"{}\" in DNA string \"{}\"".format(nb, dna))
    return "".join(dna_complement)


def reverse_complement(dna):
    """
    Return the complement of DNA string
    :param text: DNA string
    :type dna: str
    :return: complement of DNA string
    :rtype: str
    """
    dna_reverse_complement = [None] * len(dna)
    i = len(dna) - 1
    for nb in dna:
        if nb in COMPLEMENTARY_NUCLEOTIDE_MAP:
            dna_reverse_complement[i] = COMPLEMENTARY_NUCLEOTIDE_MAP[nb]
            i -= 1
        else:
            raise ValueError("Invalid nucleotide base \"{}\" in DNA string \"{}\"".format(nb, dna))
    return "".join(dna_reverse_complement)


argv = list(sys.argv)

input_dna = ""

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        input_dna += line.replace('\n', '')

try:
    output_reverse_complement = reverse_complement(input_dna)
except ValueError as err:
    output_reverse_complement = ""
    print(err)

print("The following is the reverse complement of DNA string \"{}\":\n\"{}\"".format(input_dna,
                                                                                     output_reverse_complement))

output_file = open(argv[2], 'w+')
output_file.write(output_reverse_complement)
output_file.close()
