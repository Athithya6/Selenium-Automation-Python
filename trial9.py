# Python OOPS

class Sample:  # syntax for creating a class
    word = 'Athithya'  # class variables
    numone = 1000

    def __init__(self, name, a, b):  # syntax for creating a constructor, this is a parametrized constructor
        self.name = name  # instance variables
        self.firstNum = a
        self.secNum = b
        print("I am called automatically when an object of a class is created")
        print("My name is: ",name)
        print(self.firstNum+self.secNum)

    def printNum(self):
        num = 1000
        print("This method is inside class Sample")
        print("The number is: ", num)
        c = self.firstNum + self.secNum + Sample.numone
        print("The sum is: ", c)

    def greetName(self):
        print("Hello ", self.name)
        print("I am ", Sample.word)

'''
s1 = Sample('Naveen',4,5)  # syntax to create objects in Python
s1.printNum()
print(s1.word)
s1.greetName()
'''