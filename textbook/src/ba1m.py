#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-10

Implement NumberToPattern

Implement NumberToPattern
Convert an integer to its corresponding DNA string.

Given: Integers index and k.

Return: NumberToPattern(index, k).

Sample Dataset
45
4
Sample Output
AGTC
Extra Dataset

Input
5353
7
Output
CCATGGC

Execute like:
python3 src/ba1m.py data/ba1m.txt output/ba1m.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput

if __name__ == '__main__':
    from lib.bio_util import BioUtil
else:
    from .lib.bio_util import BioUtil

argv = list(sys.argv)

input_text = ""
input_k = 0
input_mismatches = 0

for line in fileinput.input(argv[1]):
    if len(line) > 0:
        if " " in line:
            vals = line.split(" ")
            if len(vals) == 2:
                input_k = int(vals[0])
                input_mismatches = int(vals[1])
        else:
            input_text += line.replace('\n', '')


def find_frequent_words_with_mismatches(text, k, d):
    buffer = text[0:k]
    text = text[k:]
    words = dict()
    for n in BioUtil.neighbors(buffer, d):
        words[n] = 1
    for c in text:
        buffer = buffer[1:k] + c
        for n in BioUtil.neighbors(buffer, d):
            if n in words:
                words[n] += 1
            else:
                words[n] = 1
    most_frequent_words = list()
    max_frequency = 0
    for word, frequency in words.items():
        if frequency > max_frequency:
            max_frequency = frequency
            most_frequent_words = list([word])
        elif frequency == max_frequency:
            most_frequent_words.append(word)

    return most_frequent_words


frequent_words = find_frequent_words_with_mismatches(input_text, input_k, input_mismatches)

output_string = " ".join(str(i) for i in frequent_words)

print("The most frequent {}-mers with {} mismatches in \"{}\" are:\n{}".format(input_k, input_mismatches, input_text,
                                                                               output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
