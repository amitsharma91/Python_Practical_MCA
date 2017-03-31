'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python class which has two methods get_String and print_String. 
get_String accept a string from the user and print_String print the string in upper case.
'''

class StringDemo:
    def getString(self, string):
        self.string = string
    # end of method
    
    def printString(self):
        return self.string.upper()
    # end of method
# end of class

obj = StringDemo()
obj.getString("Python")  # setting String
print(obj.printString())  # printing String in upper case
