class car:

    def info(self,p_speed,p_color,p_model):
      self.speed = p_speed
      self.color = p_color
      self.model = p_model
      print(self.speed,self. color,self.model)
    def increment(self, p_speed):
        self.speed = p_speed
        print(self.speed)
    def decrement(self,p_speed):
        self.speed =self.speed- p_speed
        print(self.speed)

BMW = car()
BMW.info(320,'blue',1982)
