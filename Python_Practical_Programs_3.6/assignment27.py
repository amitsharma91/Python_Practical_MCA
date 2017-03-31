'''
Created on Mar 31, 2017

@author: developer.amit

Write a Python program to remove newline characters from a file.
'''
# open a file in write+ mode
file = open("abc.txt", "r+")

# reading contents and removing \n
contents = file.read().replace("\n", ". ")

# reset the pointer to initial position
file.seek(0)
file.truncate()  # truncate the file

# re-write the contents without new line character
file.write(contents)

print("file updated successfully...")
file.close()  # close file
