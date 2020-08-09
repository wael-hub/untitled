class A:
    def printA(self):
        print('calss A')

class B(A):
    def printB(self):
        print('class B')
objA = A()
objB = B()
objB.printA()

