'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to count the number of lines in a text file.
'''

# open file in read mode
file = open("abc.txt", "r")

count = 0

print("File contents line by line is: ")
print("*******************************")
for x in file:
    print(x)
    count += 1
# end for

print("Number of lines are: " + str(count))
