'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to find the greatest common divisor (gcd) of two integers using recursion.
'''

def gcd(n1, n2):
    if(int(n2) != 0):
        return gcd(int(n2), int(n1) % int(n2))
    else:
        return n1
# end of Method

n1 = input("Enter first Number: ")
n2 = input("Enter first Number: ")

print("G.C.D is: " + str(gcd(n1, n2)))
