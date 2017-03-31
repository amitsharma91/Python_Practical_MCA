'''
Created on Mar 25, 2017

@author: developer.amit

Write a Python program to convert a string in a list.
'''

stringData = raw_input("Enter a String: ")  # reading data

listData = stringData.split(" ")  # converting string to List 

print("String is: " + stringData)
print("List form of above string is:")
print(listData)
