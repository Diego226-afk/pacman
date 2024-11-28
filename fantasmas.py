import pyxel
import random
from Juego import Pacman
class fanta():
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        pyxel.run(self.update,self.draw)
    def draw(self):
        new_x = self.x
        new_y = self.y
    Pacman.ver_colisiones(self, new_x,new_y)
    
    def update(self):


    


        