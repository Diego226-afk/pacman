import pyxel
from pacman import Pacman as pc
class Fanta:
    def __init__(self):
        vel = 2
        self.spryte = 15

    pc.tp
    pc.ver_colisiones
    
    def update(self):
        pc.tp
        pc.ver_colisiones

    def tocar(self):
        if self.x == pc.x and self.y == pc.y:
            return True
    
    def imagenes(self):
        if pc._momento<8:
            self.cambio = 0
        if pc._momento>=8:
            self.cambio = 16

    def draw(self):
        if self.dire == "izq":
            pyxel.blt(self.x, self.y, 0 ,0 + self.cambio , 0 + 16 * self.color, 15, 15, 0)
        if self.dire == "der":
            pyxel.blt(self.x, self.y, 0,32 + self.cambio, 0 + 16 * self.color, 15, 15, 0)
        if self.dire == "arr":
            pyxel.blt(self.x, self.y, 0, 0 + self.cambio, 16 + 16 * self.color, 15, 15, 0)
        if self.dire == "abj":
            pyxel.blt(self.x, self.y, 0, 16 + self.cambio, 16 + 16 * self.color, 15, 15, 0)


class Blinky(Fanta):
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def comportamiento(self):
        
    



    



    
    




    


        