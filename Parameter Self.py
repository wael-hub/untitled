class car:

    def info(self):
        print(self.speed,self. color,self.model)
    def increment(self):
        print('increment')
    def decrement(self):
        print ('decrement')

BMW = car()
BMW.speed = 320
BMW.color = 'red'
BMW.model = 1982
BMW.info()

Camry = car()
Camry.speed = 220
Camry.color = 'blue'



