import pyxel

class Pacman:
    def __init__(self):
        pyxel.init(256, 256, title="Pacman", fps=60)
        pyxel.load("azul.pyxres") 
        self.x = 128
        self.y = 128
        self.velocidad = 2
        self.direccion = "derecha"
        self.temporizador_animacion = 0
        self.sprite_actual = 0
        self.base = 1  # Direccion horizontal
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimiento horizontal
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)) and (self.x - self.velocidad >= 0):
            self.x -= self.velocidad
            self.direccion = "izquierda"
            self.base = 1
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)) and (self.x + self.velocidad <= pyxel.width - 14):
            self.x += self.velocidad
            self.direccion = "derecha"
            self.base = -1
        
        # Movimiento vertical
        if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and (self.y - self.velocidad >= 0):
            self.y -= self.velocidad
            self.direccion = "arriba"
        if (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)) and (self.y + self.velocidad <= pyxel.height - 16):
            self.y += self.velocidad
            self.direccion = "abajo"


        # Verificar teletransporte
        self.tp()
        self.animación()
    
    def tp(self):
        if self.x == 0 and self.y == 0:
            self.x = 128
            self.y = 128  

    def animación(self):
        self.temporizador_animacion += 1
        if self.temporizador_animacion >= 10:  # Alternar sprite cada 10 frames
            self.sprite_actual = (self.sprite_actual + 1) % 2  # Alternar entre 0 y 1
            self.temporizador_animacion = 0
        
    def draw(self):
        pyxel.cls(0)  # Limpiar pantalla
        
        # Dibujar Pac-Man según la dirección
        if self.direccion == "derecha":
            pyxel.blt(self.x, self.y, 0, self.sprite_actual * 14, 0, -14, 16, 0)
        elif self.direccion == "izquierda":
            pyxel.blt(self.x, self.y, 0, self.sprite_actual * 14, 0, 14, 16, 0)
        elif self.direccion == "arriba":
            pyxel.blt(self.x, self.y, 0, self.sprite_actual * 14, 16, 14, 16, 0)
        elif self.direccion == "abajo":
            pyxel.blt(self.x, self.y, 0, self.sprite_actual * 14, 32, 14, 16, 0)

Pacman()
