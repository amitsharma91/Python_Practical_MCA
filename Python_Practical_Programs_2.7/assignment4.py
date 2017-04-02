'''
Created on Mar 25, 2017

@author: developer.amit

Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.  
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

'''
# reading string
s = raw_input("Enter Hyphen-Separated sequence word: ")

breakList = s.split("-")  # string to List
breakList.sort()  # sorting list

strNew = "-".join(breakList)  # joining List
print("Sorted data in same sequence is: " + strNew)
