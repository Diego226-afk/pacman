import pyxel
from pacman import Pacman
class Fanta:
    def __init__(self):
        self.x = 18*18
        self.y = 18*9
        self.pacman = Pacman(map)

    def update(self):
        pass



    def draw(self):
        pyxel.blt(self.x, self.y, 2, 0, 0, 16, 16, 0)  # Dibujar Fantasma como un rectangulo




    


        