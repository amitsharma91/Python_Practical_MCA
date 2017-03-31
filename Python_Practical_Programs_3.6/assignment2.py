'''
Created on Mar 31, 2017

@author: developer.amit

Write a Python program to make a chain of function decorators (bold, italic, underline etc.)
'''

def bold(name):
    def pattern():
        return "<b>" + name() + "</b>"
    # end of pattern
    return pattern
    # end pattern
# end bold

def italic(name):
    def pattern():
        return "<i>" + name() + "</i>"
    # end of pattern
    return pattern
    # end pattern
# end bold

def underline(name):
    def pattern():
        return "<u>" + name() + "</u>"
    # end of pattern
    return pattern
    # end pattern
# end bold

# decoration show method using decorators
@bold
@italic
@underline
def show():
    return "Django - Python"
# end of show


print(show())
