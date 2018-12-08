#!/usr/bin/env python

# dnaSeq = "cagagcaagactctgtctaaataaataaattaattaaattaaaaaataaataaaattgatgttttaggctaggtgtggtggctcacgcctgtaatcccagcactttgggaggccaaagtaggtggatcacctgaggtcaggagttcgagaccagcctggccaacatggtgaaaccccatctctactaaaaatacaaaaattagccgggcatagtggcgcacacctgtaatcccagcaactcgggaggctgaggcaggagaatcgcttgaacccatgtggcaaaggttgctgtgagctgagatcacaccactgtactccagcctgggcgacagagcaagactgtgtctcaattaaaaaaaattgatatttttatcaggtattaactctgaaaatacaaaaattagccaggcgtgatggcccacacctgtaatcctagctactcgggaggctgaggcacgagaatcgcctgaacctaggaggtggaggttgcagtgagctgagattgtgacactgcactccagtctggtgacagagcgagaccctctcaaaaaaaaaaaagaaaagccgagggagagaaaccttcccatttagtctgtggcatgtgtcttcatgaattgcttaagctctcaaatgttctttcagtaatttaaactcttctgctggttttcctgggaagggtgctgtataatcacatattaatgagtctttatgtgataaccttgaacaggcacgtggaggagttcagccccagagctgtctacaccagtggtaaagcgtccagtgctgctggcttaacagcagctgttgtgagagatgaagaatctcatgagtttgtcattgaggctggagctttgatgttggctgataatgtaagaacattttacactcttcagtataaagaagtcagaatacccctaccctatcagtaaaggcctataagttaccattaaaaagatgtccttaaaaacagcattctcagctgggcgcggtggctcacacctttgtcccagtactttgggaagccgaggtgggtggatcacctgaggtcaggagttcgagaccagcctggccaacatggcgaaaacccattttctctactaaaaatacaaaaattagccgggcatggtggcgggtgcttgt"

dnaSeq = input ("Type DNA Sequence:")

# Calculate total sequence length
print ("total sequence length")
print (len(dnaSeq))

#use this to count number of As
print  ("Number of As:")
print (dnaSeq.lower().count('a'))

print ("Number of C's")
print (dnaSeq.lower().count ('c'))

print ("Number of Gs")
print (dnaSeq.lower().count ('g'))

print ("Number of Ts")
print (dnaSeq.lower().count ('t'))

# DB: Good, although this won't count properly if the sequence is provided in uppercase.
#     One way to avoid this problem is to add .lower() after dnaSeq (see above). Also, it's
#     a good idea to only use .sh in file names for shell scripts. Instead, use .py for
#     Python code.