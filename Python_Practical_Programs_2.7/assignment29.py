'''
Created on Mar 24, 2017

@author: developer.amit

Write a Python program to construct the following pattern, using a nested loop number.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
'''

import sys

for i in range(1, 10):
    for j in range(1, (i + 1)):
        sys.stdout.write(str(i) + " ");
    print("")
    # end of Inner For
# end of outer for
