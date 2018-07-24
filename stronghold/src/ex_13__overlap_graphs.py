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


def build_adjacency_matrix(edge_map, k=3):
    """
    :param edge_map: map of ID to DNA string
    :type edge_map: dict
    :param k: size of overlap
    :type k: int
    :return: adjacency matrix, a list of 2-element lists, where each element is a tuple of node label and DNA string
    :rtype: [[(list, str)]]
    """
    adjancency_matrix = []
    prefix_map = dict()

    for label, dna in edge_map.items():
        prefix = dna[:k]
        if prefix in prefix_map:
            prefix_map[prefix].append((label, dna))
        else:
            prefix_map[prefix] = [(label, dna)]

    for label, dna in edge_map.items():
        suffix = dna[-k:]
        if suffix not in prefix_map:
            continue
        matches = prefix_map[suffix]
        for match in matches:
            if match[1] == dna:  # Criteria to prevent directed loops (unpack DNA string from tuple (2nd element))
                continue
            adjancency_matrix.append([(label, dna), match])

    return adjancency_matrix


def init_edge_map(filename):
    """
    :param filename: file name
    :type filename: str
    :return: edge_map: map of ID to DNA string
    :rtype: dict
    """
    edge_map = dict()
    dna_id = None
    dna_string_builder = []

    for line in fileinput.input(filename):
        if line.startswith(">"):
            if dna_id is not None:
                edge_map[dna_id] = "".join(dna_string_builder)
            dna_id = line.replace(">", "").replace("\n", "")
            dna_string_builder = []
        elif len(line) > 0:
            dna_string_builder.extend(list(line.replace("\n", "")))    # DNA string can span multiple lines

    if dna_id is not None and len(dna_string_builder) > 0:
        edge_map[dna_id] = "".join(dna_string_builder)

    return edge_map


k = 3
edge_map = init_edge_map(argv[1])
adjacency_matrix = build_adjacency_matrix(edge_map, 3)

# For output, separate out labels
output_adjacency_lists = []
for adjacency_list in adjacency_matrix:
    labels, dna_strings = map(list, zip(*adjacency_list))
    output_adjacency_lists.append(labels)

output_file = open(argv[2], 'w+')
for output_adjacency_list in output_adjacency_lists:
    output_file.write(" ".join(output_adjacency_list) + '\n')
output_file.close()

