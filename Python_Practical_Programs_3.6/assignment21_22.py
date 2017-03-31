'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to read a file line by line store it into a variable.
'''

# open file in read mode
file = open("abc.txt", "r")

print("File contents line by line: ")
print("****************************")

lines = []  # list to store lines of file

for x in file:
    print(x)
    lines.append(x)  # adding each line to list

file.close()  # close file
