'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
e.g
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
'''

import sys

class SumOfThreeToZero:
    def __init__(self, list1):
        self.list1 = list1
    # end of constructor
    
    def checkSum(self):
        n = len(self.list1)
        
        sys.stdout.write("[")
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if(self.list1[i] + self.list1[j] + self.list1[k] == 0):
                        sys.stdout.write("[" + str(self.list1[i]) + ", " + str(self.list1[j]) + ", " + str(self.list1[k]) + "],")
                    # end if
                # end k-for
            # end j-for
        # end i-for
        sys.stdout.write("]")
    # end of method
# end of class

# defining List
list1 = [-25, -10, -7, -3, 2, 4, 8, 10]

# creating Object
obj = SumOfThreeToZero(list1)

print("Sum of 3 element to ZERO is: ")
obj.checkSum()
