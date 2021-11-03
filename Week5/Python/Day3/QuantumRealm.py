import random


class QuantumParticle:
    def __init__(self,x,y,p):
        self.x=x
        self.y=y
        self.p=p

    def position(self):
        self.x=random.randint(1,10000)

    def momentum(self):
        self.y=random.random()

    def spin(self):
        p=random.choice([-0.5,0.5])