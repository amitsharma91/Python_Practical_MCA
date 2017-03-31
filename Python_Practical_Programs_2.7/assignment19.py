'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to read an entire text file. 
'''

# open file in read mode
file = open("abc.txt", "r")

content = file.read();  # read contents of file
print("Contents of file: ")
print("*******************")
print(content)

file.close()  # close file
