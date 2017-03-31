'''
Created on Mar 31, 2017

@author: developer.amit

Write a Python program to combine each line from first file with the corresponding line in second file.
'''

import sys

# open both files and print each line combined 
with open("pqr.txt") as f1, open("xyz.txt") as f2:
    for l1, l2 in zip(f1, f2):
        sys.stdout.write(str(l1.replace("\n", ". ")) + "" + str(l2))

