__author__ = 'johndibaggio'

from abc import ABCMeta
from collections import deque

A = 'A'
C = 'C'
G = 'G'
T = 'T'

NUCLEOTIDES = [A, C, G, T]


class BioUtil:
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Empty __init__
        """

    @staticmethod
    def symbol_to_number(symbol):
        if symbol == A:
            return 0
        elif symbol == C:
            return 1
        elif symbol == G:
            return 2
        elif symbol == T:
            return 3
        return 0

    @staticmethod
    def number_to_symbol(index):
        if index == 0:
            return A
        elif index == 1:
            return C
        elif index == 2:
            return G
        elif index == 3:
            return T
        return ''

    @staticmethod
    def suffix(pattern):
        """
        Return a (k-1)-mer by taking the nucleotides of pattern after the first one
        :param pattern:
        :type pattern: str
        :return:
        :rtype: str
        """
        return pattern[1:]

    @staticmethod
    def first_symbol(pattern):
        return pattern[0:1]

    @staticmethod
    def pattern_to_number(pattern):
        if pattern is None or len(pattern) == 0:
            return 0
        last_symbol = pattern[-1:]
        prefix = pattern[:-1]
        return 4 * BioUtil.pattern_to_number(prefix) + BioUtil.symbol_to_number(last_symbol)

    @staticmethod
    def number_to_pattern(index, k):
        if k == 1:
            return BioUtil.number_to_symbol(index)
        prefix_index = index // 4
        r = index % 4
        symbol = BioUtil.number_to_symbol(r)
        prefix_pattern = BioUtil.number_to_pattern(prefix_index, k - 1)
        return prefix_pattern + symbol

    @staticmethod
    def neighbors(pattern, d):
        if d == 0:
            return [pattern]
        if len(pattern) == 1:
            return NUCLEOTIDES
        neighborhood = set()
        suffix_neighbors = BioUtil.neighbors(BioUtil.suffix(pattern), d)
        for text in suffix_neighbors:
            if BioUtil.hamming_distance(BioUtil.suffix(pattern), text) < d:
                for n in NUCLEOTIDES:
                    neighborhood.add(n + text)
            else:   # Hamming distance == d
                neighborhood.add(BioUtil.first_symbol(pattern) + text)
        return neighborhood

    @staticmethod
    def hamming_distance(p, q):
        """
        Return integer value representing the Hamming distance between DNA strings p and q
        :param p: DNA string 1
        :type p: str
        :param q: DNA string 2
        :type q: str
        :return: Hamming distance between DNA strings p and q
        :rtype: int
        """
        mismatches = 0
        p_bases = deque(p)
        q_bases = deque(q)
        while len(p_bases) > 0 and len(q_bases) > 0:
            if p_bases.popleft() != q_bases.popleft():
                mismatches += 1
        return mismatches

    @staticmethod
    def approximate_pattern_count(pattern, text, d):
        """
        Find all starting positions where pattern appears as a substring of text with at most d mismatches.
        :param pattern:
        :type pattern: str
        :param text:
        :type text: str
        :param d:
        :type d: int
        :return: list of all starting positions where pattern appears as a substring of text with at most d mismatches.
        :rtype: list[int]
        """
        k = len(pattern)
        buffer = text[0:k]
        text = text[k:]
        i = 0
        indices = []
        if BioUtil.hamming_distance(buffer, pattern) <= d:
            indices.append(i)
        for c in text:
            i += 1
            buffer = buffer[1:k] + c
            if BioUtil.hamming_distance(buffer, pattern) <= d:
                indices.append(i)
        return indices


# BioUtil.register(tuple)
#
# assert issubclass(tuple, BioUtil)
# assert isinstance((), BioUtil)
