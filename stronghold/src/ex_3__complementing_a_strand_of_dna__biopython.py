#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
"""
__author__ = 'johndibaggio'

import sys
import os
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

argv = list(sys.argv)
input_file = open(argv[1])
output_file = open(argv[2], 'w+')

dna = input_file.read()

dna_sequence = Seq(dna, IUPAC.unambiguous_dna)

reverse_complement = dna_sequence.reverse_complement()

output_file.write(str(reverse_complement))
output_file.close()
input_file.close()
