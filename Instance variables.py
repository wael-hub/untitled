class car:

    def increment(self):
        print('increment')
    def decrement(self):
        print ('decrement')

BMW = car()
BMW.speed = 320
BMW.color = 'red'
print(BMW.speed)

Camry = car()
Camry.speed = 220
Camry.color = 'blue'
print(Camry.color)


