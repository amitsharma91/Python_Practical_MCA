'''
Created on Mar 29, 2017

@author: developer.amit

Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''

#method to get List with unique Elements
def unique_list(list):
    return set(list)
#end of method

#define a list
list1 = [5,6,4,5,56,5,6,6,66,2,5,66,3,2,5,6,6,2,45,65]

print("List with duplicate Elements:")
print(list1)
print("List with Unique Elements:")
print(unique_list(list1))