import pyxel

class Pacman:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  
        self.speed = 5  

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.speed
        if pyxel.btn(pyxel.KEY_W):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.speed

    def draw(self):

        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)

def update():
    player.update()  

def draw():
    pyxel.cls(0)  
    player.draw()  

pyxel.init(256, 256, title="Mi Juego")  

pyxel.load("pacman.pyxres")  

player = Pacman(128, 128)

pyxel.run(update, draw)  