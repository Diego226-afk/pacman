import pyxel
from pacman import Pacman
from Mapas import Map
from fanta_v2 import Blinky, Pinky, Inky, Clyde

class App():
    def __init__(self):
        # Inicializar Pyxel y cargar recursos
        pyxel.init(18*36, 19*18, title="Pacman", fps=60)
        pyxel.load("pacman.pyxres")

        # Crear instancias del mapa y Pacman
        self.mapa = Map()
        self.pacman = Pacman(self.mapa)

        # Crear los fantasmas con posiciones iniciales y colores únicos
        self.fantasmas = [
            Blinky(18 * 9, 18 * 8, 48, self.mapa),  # Fantasma rojo
            Pinky(18 * 10, 18 * 8, 64, self.mapa),  # Fantasma rosado
            Inky(18 * 11, 18 * 8, 80, self.mapa),   # Fantasma azul
            Clyde(18 * 12, 18 * 8, 96, self.mapa),  # Fantasma naranja
        ]

        # Ejecutar el juego
        pyxel.run(self.update, self.draw)

    def update(self):
        """Actualizar la lógica del juego"""
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # Actualizar Pacman
        self.pacman.update()

        # Obtener coordenadas de Blinky para Inky
        blinky_x, blinky_y = self.fantasmas[0].x, self.fantasmas[0].y

        # Actualizar cada fantasma
        for fantasma in self.fantasmas:
            if isinstance(fantasma, Inky):
                fantasma.update(self.mapa, self.pacman.x, self.pacman.y, blinky_x, blinky_y)
            else:
                fantasma.update(self.mapa, self.pacman.x, self.pacman.y)

    def draw(self):
        """Dibujar todos los elementos en pantalla"""
        pyxel.cls(0)  # Limpiar la pantalla
        self.mapa.draw()  # Dibujar el mapa
        self.pacman.draw()  # Dibujar Pacman
        for fantasma in self.fantasmas:  # Dibujar los fantasmas
            fantasma.draw()

# Ejecutar la aplicación
App()

