import pyxel

class Pacman:
    def __init__(self):
        pyxel.init(256, 256, title="Pacman", fps=60)  # Iniciar Pyxel
        pyxel.load("azul.pyxres")  # Cargar tu archivo de recursos
        
        self.x = 120  # Posición inicial en x
        self.y = 120  # Posición inicial en y
        self.velocidad = 2  # Velocidad de movimiento
        self.sprite_actual = 0  # Índice del sprite (0 o 1)
        self.temporizador_animacion = 0  # Temporizador para animación

        pyxel.run(self.update, self.draw)  # Ejecutar el juego

    def update(self):
        # Movimiento básico del personaje
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidad
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidad
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidad
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidad

        # Animación del sprite
        self.temporizador_animacion += 1
        if self.temporizador_animacion >= 8:  # Cambiar sprite cada 8 frames
            self.sprite_actual = (self.sprite_actual + 1) % 2
            self.temporizador_animacion = 0

    def draw(self):
        pyxel.cls(0)  # Limpiar la pantalla (color negro)
        # Dibujar el sprite basado en el índice actual
        pyxel.blt(self.x, self.y, 0, self.sprite_actual * 16, 0, 16, 16, 0)

# Ejecutar la clase Pacman
Pacman()
