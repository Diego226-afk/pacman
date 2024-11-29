import pyxel
from pacman import Pacman
from Mapas import Map

class App():
    def __init__(self):
        pyxel.init(18*36, 19*18, title="Pacman", fps=60)
        pyxel.load("pacman.pyxres")

        # Crear instancias de Pacman, Mapita y Fanta
        self.mapa = Map()  # Pasar la instancia del mapa
        self.pacman = Pacman(self.mapa)  # Pasar la instancia del mapa a Pacman

    def update(self):
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # Actualizar los elementos del juego
        self.pacman.update()  # Actualizar Pacman

    def draw(self):
        pyxel.cls(0)  # Limpiar la pantalla

        # Dibujar los elementos del juego
        self.mapa.draw()  # Dibujar el mapa
        self.pacman.draw()  # Dibujar Pacman

# Ejecutar la aplicación
App()