class A:
    def printA(self):
        print('calss A')

class B(A):
    def printB(self):
        print('class B')
        super().printA()



objA = A()
objB = B()
objB.printB()


