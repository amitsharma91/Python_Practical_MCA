'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program to read first n lines of a file
'''

# Open File in read mode
file = open("abc.txt", "r")

n = input("Enter the number of lines to be printed: ")

lines = [next(file) for x in range(int(n))]

print("First " + str(n) + " lines are: ")
print("*********************")

for l in lines:
    print(l)
# end of for

file.close()  # close file
