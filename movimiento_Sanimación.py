import pyxel

class Pacman:
    def __init__(self):
        pyxel.init(256, 256, title="Pacman", fps=100)
        pyxel.load("pacman.pyxres") 
        self.x = 128
        self.y = 128
        self.velocidad = 2
        self.direccion = "derecha"
        self.temporizador_animacion = 0
        self.sprite_actual = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimiento y cambio de dirección
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)) and (self.x - self.velocidad >= 0):
            self.x -= self.velocidad
            self.direccion = "izquierda"
            self.base = 1
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)) and (self.x + self.velocidad <= pyxel.width - 15):
            self.x += self.velocidad
            self.direccion = "derecha"
            self.base = -1
        if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and (self.y - self.velocidad >= 0):
            self.y -= self.velocidad
            self.direccion = "arriba"
        if (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)) and (self.y + self.velocidad <= pyxel.height - 16):
            self.y += self.velocidad
            self.direccion = "abajo"
        
        # Comprobar teletransporte
        self.tp()

    def tp(self):
        if self.x==0 and self.y==0:
            self.x=128
            self.y=128

    def draw(self):
        pyxel.cls(0)  # Limpiar pantalla
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 17, 0)

class Fant:
    pass
Pacman()
