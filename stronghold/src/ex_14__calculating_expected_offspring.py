#!/usr/bin/env
# encoding: utf-8
"""
For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

1. AA-AA  - 100%
2. AA-Aa  - 100%
3. AA-aa  - 100%
4. Aa-Aa  - 75%
5. Aa-aa  - 50%
6. aa-aa  - 0%
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1
Sample Output
3.5

Execute like:
python src/ex_14__calculating_expected_offspring.py data/ex_14.txt output/ex_14.txt

"""
__author__ = 'johndibaggio'

import sys
import numpy

argv = list(sys.argv)

# % probabilities of dominant phenotype for [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
PROBABILITIES_PERCENTAGES = [100, 100, 100, 75, 50, 0]
# 2 offspring per couple
MULTIPLIER = 2


def calculate_num_offspring(couples, probabilities, multiplier):
    """
    Calculate the expected number of offspring displaying the dominant phenotype in the next generation
    :param couples: list of numbers of couples in a population possessing each genotype pairing for a given factor
    :type couples: list[int]
    :param probabilities: list of probability percentages of offspring expressing dominant phenotype for the given factor
    :type probabilities: list[int]
    :param multiplier: number of offspring per couple
    :type multiplier: int
    :return: total number of expected offspring
    :rtype: float
    """
    offspring = numpy.multiply(couples, probabilities)            # multiply couples by probabilities
    offspring = numpy.divide(offspring, 100)                      # divide by 100%
    offspring = numpy.multiply(offspring, multiplier, offspring)  # multiply by 2 offspring/couple, in-place multiply
    return numpy.sum(offspring)                                   # sum offspring to get total expected


def get_couples(filename):
    """
    Get list of integer numbers of couples from file
    :param filename: file name
    :type filename: str
    :return: edge_map: map of ID to DNA string
    :rtype: list[int]
    """
    file = open(filename)
    line = file.readline()
    file.close()

    strings = line.replace('\n', "").split(" ")
    couples = [0] * len(strings)
    for i in range(0, len(strings)):
        couples[i] = int(strings[i])

    return couples


input_couples = get_couples(argv[1])
num_offspring_expected = calculate_num_offspring(input_couples, PROBABILITIES_PERCENTAGES, MULTIPLIER)

print("Expected number of offspring expressing dominant phenotype from set of couples {}: {}"
      .format(input_couples, num_offspring_expected))

output_file = open(argv[2], 'w+')
output_file.write(str(num_offspring_expected))
output_file.close()

