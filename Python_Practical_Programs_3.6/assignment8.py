'''
Created on Mar 25, 2017

@author: developer.amit

Write a Python function to multiply all the numbers in a list.
'''
from pip._vendor.distlib.compat import raw_input

#method to multiply all List Numbers
def multiplyList(listData):
    prod = 1
    for x in listData:
        prod *= x
    #end of for
    return prod;
#end of Method

print("Enter some numbers for List: ")
#accept number list from user
listData = map(int,raw_input().split())

print("Multiplication of all numbers in list is: "+str(multiplyList(listData)))