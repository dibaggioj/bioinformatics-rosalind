#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-07-22

This is the first problem in a collection of "code challenges" to accompany Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.

A k-mer is a string of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text. For example,

Count(ACAACTATGCATACTATCGGGAACTATCCT,ACTAT)=3.
We note that Count(CGATATATCCATAG, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.

To compute Count(Text, Pattern), our plan is to “slide a window” down Text, checking whether each k-mer substring of Text matches Pattern. We will therefore refer to the k-mer starting at position i of Text as Text(i, k). Throughout this book, we will often use 0-based indexing, meaning that we count starting at 0 instead of 1. In this case, Text begins at position 0 and ends at position |Text| − 1 (|Text| denotes the number of symbols in Text). For example, if Text = GACCATACTG, then Text(4, 3) = ATA. Note that the last k-mer of Text begins at position |Text| − k, e.g., the last 3-mer of GACCATACTG starts at position 10 − 3 = 7. This discussion results in the following pseudocode for computing Count(Text, Pattern).

Implement PatternCount
Given: {DNA strings}} Text and Pattern.

Return: Count(Text, Pattern).

PatternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
                count ← count + 1
        return count

"""
__author__ = 'johndibaggio'

import sys
import fileinput


def pattern_count(text, pattern):
    """
    Find the frequency of the pattern in the text
    :param text: DNA/RNA string
    :type text: str
    :param pattern: k-mer pattern to find in text
    :type pattern: str
    :return: frequency of pattern in text
    :rtype: int
    """
    count = 0
    k = len(pattern)
    for i in range(0, len(text) - (k - 1)):
        if text[i:i+k] == pattern:
            count += 1
    return count


argv = list(sys.argv)

input_text = None
input_pattern = None

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if input_text is None:
            input_text = line.replace('\n', '')
        elif input_pattern is None:
            input_pattern = line.replace('\n', '')

output_count = pattern_count(input_text, input_pattern)

print("The pattern \"{}\" appears in \"{}\" {} time(s)".format(input_pattern, input_text, output_count))

output_file = open(argv[2], 'w+')
output_file.write(str(output_count))
output_file.close()

