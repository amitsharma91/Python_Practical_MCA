'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. 
e.g.
Input: numbers= [20,10,40,50,60,70], target=50
Output: 2,3
'''

class SumIndices:
    def __init__(self, list1, target):
        self.list = list1
        self.target = target
    # end of constructor
    
    # method to print Indices
    def printIndices(self):
        i = 0
        n = len(self.list)
        while(i < n):
            j = i
            while(j < (n - 1)):
                if((self.list[i] + self.list[j]) == int(self.target)):
                    print("Indices for target - " + str(self.target) + " are: ")
                    print(str(i) + "," + str(j))
                # end of if
                j += 1   
            # end f inner while
            i += 1
        # end of outer while
    # end of method
# end of class 

# define List
list1 = [20, 10, 40, 50, 60, 70]
tar = input("Enter the Element for Target: ")

# create object
obj = SumIndices(list1, tar)
obj.printIndices()
