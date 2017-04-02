'''
Created on Mar 31, 2017

@author: developer.amit

Write a Python function that that prints out the first n rows of Pascal's triangle.
'''
import sys

def printPascalTriangle(rows):
    for i in range(0, int(rows)):
        val = 1
        for j in range(1, int(rows) - 1):
            sys.stdout.write(" ")
        # end j-for
        for k in range(0, (i + 1)):
            sys.stdout.write(" " + str(val))
            val = int(val * (i - k) / (k + 1))
        # end k-for
        print("")
        print("")  
    # end i-for
    print("")
# end of Method


n = input("Enter number of Rows: ")

printPascalTriangle(n)
