# Python OOPS

class Sample():  #syntax for creating a class
    word = 'Athithya'  #class variables

    def __init__(self): #syntax for creating a constructor
        print("I am called automatically when an object of a class is created")

    def printNum(self):
        num = 1000
        print("This method is inside class Sample")
        print("The number is: ", num)


s1 = Sample()  # syntax to create objects in Python
s1.printNum()
print(s1.word)

s2=Sample()
s2.printNum()
print(s2.word)
