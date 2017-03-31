'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to get the factorial of a non-negative integer using recursion.
'''

def factorial(num):
    n = int(num)
    if(n == 1):
        return 1;
    elif(n < 0):
        print("Factorial cannot be calculated")
        return
    else:
        fact = n * factorial(n - 1)
        return fact
# end of method

num = input("Enter a non-negative number: ")

print("Factorial is: " + str(factorial(num)))
