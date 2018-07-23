#!/usr/bin/env
# encoding: utf-8
"""
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Execute like:
python src/ex_13__overlap_graphs.py data/ex_13.txt output/ex_13.txt

"""
__author__ = 'johndibaggio'

import sys
import fileinput

argv = list(sys.argv)


def build_adjacency_lists(edge_map, k=3):
    adjancency_lists = []
    for label, dna


edge_map = dict()


def init_edge_map():
    dna_id = None
    for line in fileinput.input(argv[1]):
        if line.startswith('>'):
            dna_id = line.replace('>', '').replace('\n', '')
        elif len(line) > 0:
            dna_string = line.replace('\n', '')
            if dna_id is not None:
                edge_map[dna_id] = dna_string
                dna_id = None


init_edge_map()

print(edge_map)
# output_freq_words = frequent_words(input_text, input_k)
# most_freq_kmer_list = output_freq_words[0]
# greatest_freq = output_freq_words[1]
#
# output_most_freq_kmers = " ".join(most_freq_kmer_list)
#
# print("The following most frequent {}-mers in \"{}\" each have a frequency of {}:\n{}".format(input_k,
#                                                                                             input_text,
#                                                                                             str(greatest_freq),
#                                                                                             output_most_freq_kmers))
#
# output_file = open(argv[2], 'w+')
# output_file.write(output_most_freq_kmers)
# output_file.close()

