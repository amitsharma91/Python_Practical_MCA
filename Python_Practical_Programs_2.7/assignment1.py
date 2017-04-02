'''
Created on Mar 24, 2017

@author: developer.amit

Write a Python program to detect the number of local variables declared in a function
'''
# user-defined method
def myMethod():
    a = 1;
    b = 2.5;
    c = "Three";
#end of method
    
    print(str(a) + "\n" + str(b) + "\n" + str(c))
# end of Method

# printing local variables form user-defined Method
print("Number of Local Variables: " + str(myMethod.__code__.co_nlocals)); 
