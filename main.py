import pyxel
from pacman import Pacman
from Mapas import Map
from fantasmas import Fanta

class App():
    def __init__(self):
        pyxel.init(18*36, 19*18, title="Pacman", fps=60)
        pyxel.load("pacman.pyxres")

        # Crear instancias de Pacman, Mapita y Fanta
        self.mapa = Map()  # Pasar la instancia del mapa
        self.pacman = Pacman(self.mapa)  # Pasar la instancia del mapa a Pacman
        self.fantasma = Fanta()
    
    def dibu():
        pyxel.blt(18, 18, 0, 0, 32, 16, 16, 0)


    def update(self):
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # Actualizar los elementos del juego
        self.pacman.update()  # Actualizar Pacman
        self.fantasma.update()  # Actualizar Fanta
        self.dibu()

    def draw(self):
        pyxel.cls(0)  # Limpiar la pantalla
        pyxel.text(10, 10, f"{self._contador} puntos", 8)
        

        # Dibujar los elementos del juego
        self.mapa.draw()  # Dibujar el mapa
        self.dibu()
        self.pacman.draw()  # Dibujar Pacman
        self.fantasma.draw()  # Dibujar Fanta

# Ejecutar la aplicación
App()