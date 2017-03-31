'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python class to implement pow(x, n).
'''

class Power:
    # method to calculate Power
    def pow(self, x, n):
        return int(x) ** int(n)
    # end of method
# end of class 

x = input("Enter the Base: ")
n = input("Enter the Index: ")

# crate object
obj = Power()
print("Power is: " + str(obj.pow(x, n)))
