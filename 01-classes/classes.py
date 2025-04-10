class Ponto:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def quadrante(self):
        if self.x > 0 and self.y >0:
            return 'Q1'
        elif self.x < 0 and self.y >0:
            return 'Q2'
        elif self.x < 0 and self.y < 0:
            return '3'
        elif self.x > 0 and self.y < 0:
            return 'Q4'

p1 = Ponto(1,-1,)
print(p1.quadrante())