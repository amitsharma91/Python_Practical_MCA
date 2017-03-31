'''
Created on Mar 25, 2017

@author: developer.amit

Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
'''

# method to count upper n Lower case
def countCases(stringData):
    upper = 0;
    lower = 0;
    for s in stringData:
        if(s.islower()):
            lower += 1
        if(s.isupper()):
            upper += 1
    # end of for
    print("Number of UpperCase letters: " + str(upper))
    print("Number of lowerCase letters: " + str(lower))
# end of Method

stringData = raw_input("Enter some String: ");
countCases(stringData)
