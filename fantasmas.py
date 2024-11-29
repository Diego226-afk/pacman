import pyxel
class Fanta:
    def __init__(self, pacman):
        self.x = 18*18
        self.y = 18*9
        self.pacman = pacman

    def update(self):
        pass

    

    def draw(self):
        pyxel.blt(self.x, self.y, 2, 0, 0, 16, 16, 0)  # Dibujar Fantasma como un rectangulo




    


        