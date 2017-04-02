import os
from sys import exit

#Will be a series of functions that I call with different argumentrs
class me(object):
    print "me"

print me
def func1():
    print "test, enter a number"
    number = raw_input("> ")
    test = raw_input("> ")
    while test == "0":
        print "test is 0"
        break

    if number == "1" and test == "1":
        print "1"
    elif number == "2" and test == "2":
        print "2"
    else:
        assert number is 2

def func2():
    apple = lambda a: a + a
    print apple(4)
def func3():
    pass


print "Call test function"
print "enter number of function"
function =  raw_input("> ")
if function == "1":
    func1()
elif function == "2":
    func2()
elif function == "3":
    func3()
