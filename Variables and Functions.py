

    def info(self):
        print(self.speed,self. color,self.model)
    def increment(self, p_speed):
        self.speed = p_speed
        print(self.speed)
    def decrement(self,p_speed):
        self.speed =self.speed- p_speed
        print(self.speed)

BMW = car()
BMW.speed = 320
BMW.color = 'red'
BMW.model = 1982
BMW.info()
BMW.increment(80)
BMW.decrement(20)
