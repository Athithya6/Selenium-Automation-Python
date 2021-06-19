# Inheritance in Python OOPS
from trial9 import Sample


class Sample1(Sample):
    num4 = 500

    def __init__(self):
        Sample.__init__(self, 'Aparna', 12, 10)

    def getComplete(self):
        print(self.num4 + self.numone)
        print(self.greetName())


s2 = Sample1()
s2.getComplete()
