'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
'''

class Rectangle:
    # constructor
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
    # end of Constructor
    
    def area(self):
        return (self.length * self.width)
    # end of method
# end class

leng = input("Enter Length: ")
wid = input("Enter Width: ")

# create Object
obj = Rectangle(leng, wid)
print("Area of Rectangle is: " + str(obj.area()))
