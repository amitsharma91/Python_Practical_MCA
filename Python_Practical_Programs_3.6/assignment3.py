'''
Created on Mar 25, 2017

@author: developer.amit

Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
'''
import sys

# declaring a list
listData = list()

# method to create,print list of squares
def listOfSquares(maxNum):
    for num in range(1,int(maxNum)+1):
        listData.append(num * num)
    # end of for
    
    # printing list elements:
    for num in listData:
        sys.stdout.write(str(num) + "\t")
# end of method

maxNum = input("Enter the Upper Limit for List: ")
listOfSquares(maxNum)
