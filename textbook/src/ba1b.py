#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-07-22

We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

Frequent Words Problem

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).

Execute like:
python src/ba1b.py data/ba1b.txt output/ba1b.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput


def frequent_words(text, k):
    """
    Find the most frequent k-mer(s) in text and their frequency
    :param text: DNA/RNA string
    :type text: str
    :param k: size of substring pattern
    :type k: int
    :return: tuple of list of most frequent k-mer(s) in text and the frequency, ([kmer1,kmer2,...], frequency)
    :rtype: (list, int)
    """
    freq_table = dict()
    for i in range(0, len(text) - (k - 1)):
        kmer = text[i:i+k]
        if kmer in freq_table:
            freq_table[kmer] += 1
        else:
            freq_table[kmer] = 0
    greatest_freq = 0
    most_freq_kmers = []
    for kmer, freq in freq_table.items():
        if freq > greatest_freq:
            greatest_freq = freq
            most_freq_kmers = [kmer]
        elif freq == greatest_freq:
            most_freq_kmers.append(kmer)

    return most_freq_kmers, greatest_freq


argv = list(sys.argv)

input_text = None
input_k = 0

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if input_text is None:
            input_text = line.replace('\n', '')
        elif input_k == 0:
            input_k = int(line.replace('\n', ''))

output_freq_words = frequent_words(input_text, input_k)
most_freq_kmer_list = output_freq_words[0]
greatest_freq = output_freq_words[1]

output_most_freq_kmers = " ".join(most_freq_kmer_list)

print("The following most frequent {}-mers in \"{}\" each have a frequency of {}:\n{}".format(input_k,
                                                                                            input_text,
                                                                                            str(greatest_freq),
                                                                                            output_most_freq_kmers))

output_file = open(argv[2], 'w+')
output_file.write(output_most_freq_kmers)
output_file.close()

