'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to copy the contents of a file to another file.
'''

# open first file in read mode
file1 = open("abc.txt", "r")

contents1 = file1.read()  # read file1 contents into string

# open another file in write mode to copy
file2 = open("pqr.txt", "w")

file2.write(contents1)  # writing file1 contents to file2
print("File copied")

file1.close()  # close file1
file2.close()  # close file
