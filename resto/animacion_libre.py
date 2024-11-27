import pyxel

class Pacman:
    def __init__(self):
        pyxel.init(256, 256, title="Pacman", fps=100)
        pyxel.load("azul.pyxres") 
        self.x = 128
        self.y = 128
        self.velocidad = 2
        self.direccion = "derecha"
        self.temporizador_animacion = 0
        self.sprite_actual = 0
        self.base = 1
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
        
        # Animación del sprite
        self.temporizador_animacion += 1
        if self.temporizador_animacion >= 8:  # Cambiar sprite cada 8 cuadros
            self.sprite_actual = (self.sprite_actual + 1) % 2
            self.temporizador_animacion = 0
        
        # Comprobar teletransporte
        self.tp()

    def tp(self):
        # Teletransportar entre los bordes del mapa
        if self.x < 0:
            self.x = pyxel.width - 15
        elif self.x > pyxel.width - 15:
            self.x = 0
        if self.y < 0:
            self.y = pyxel.height - 16
        elif self.y > pyxel.height - 16:
            self.y = 0

    def draw(self):
        pyxel.cls(0)  # Limpiar pantalla
        
        # Ajustar sprite según la dirección
        sprite_x = self.sprite_actual * 14
        pyxel.blt(self.x, self.y, 0, self.sprite_actual * 16, 0, 16, 16, 0)
Pacman()
