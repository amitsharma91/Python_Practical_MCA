'''
Created on Mar 30, 2017

@author: developer.amit

Write a Python program of recursion list sum. 
Test Data : [1, 2, [3,4], [5,6] ] Expected Result : 21
'''
# define a list
a = [1, 2, [3, 4], [5, 6] ]

sum = 0  # initializing sum to 0

# iterating through List and adding
for i in a:
    if isinstance(i, list):
        for j in i:
            sum += j
        # end for
    # end if
    else:
        sum += i
# end for

print("Recursive list:")    
for x in a:
	print(x)

print("Sum of elements is: " + str(sum))
