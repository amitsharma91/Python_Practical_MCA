'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
'''

class Circle:
    # class variable
    PI = 3.1421  
    
    # constructor
    def __init__(self, radius):
        self.radius = int(radius)
    # end of constructor
    
    def area(self):
        return (2 * Circle.PI * self.radius * self.radius)
    # end of method
    
    def perimeter(self):
        return (2 * Circle.PI * self.radius)
    # end of method
# end of class

rad = input("Enter Radius: ")

# create Object
obj = Circle(rad)

print("Area is: " + str(obj.area()))
print("Perimeter is: " + str(obj.perimeter()))
