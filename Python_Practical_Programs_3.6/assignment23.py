'''
Created on Mar 30, 2017

@author: developer.amit

Write a python program to find the longest words. 
'''

# open file in read mode
file = open("abc.txt", "r")

content = file.read()  # read all contents into variable
newCon = content.replace("\n", " ")  # replacing \n with " "
br = newCon.split(" ")  # convert string to list

print("The longest Word in File is: ")
print(max(br, key=len))  # max element from list

file.close()  # close file
