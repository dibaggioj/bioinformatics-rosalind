#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2018-08-08

Find the Most Frequent Words with Mismatches in a String solved by 486

We defined a mismatch in “Compute the Hamming Distance Between Two Strings”. We now generalize “Find the Most Frequent
Words in a String” to incorporate mismatches as well.

Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of
occurrences of Pattern in Text with at most d mismatches. For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 because AAAAA appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among
all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, AAAAA is the most
frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though AAAAA does not appear exactly in this string.
Keep this in mind while solving the following problem.

Frequent Words with Mismatches Problem
Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d, where k ≤ 12 and d ≤ 3

Return: All most frequent k-mers with up to d mismatches in Text.

Sample Dataset:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1
Sample Output:
GATG ATGC ATGT

Sample Dataset:
CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC
10 2
Sample Output:
GCACACAGAC GCGCACACAC

Execute like:
python3 src/ba1i.py data/ba1i.txt output/ba1i.txt

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

print("The most frequent {}-mers with {} mismatches in \"{}\" are:\n{}".format(input_k, input_mismatches, input_text, output_string))

output_file = open(argv[2], "w+")
output_file.write(output_string)
output_file.close()
