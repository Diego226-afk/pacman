import pyxel
from pacman import Pacman
class Map:
    def __init__(self, niveles):
        self.niveles = niveles  # Lista de niveles
        self.nivel_actual = 0  # Empieza en el primer nivel
        self.maze = self.niveles[self.nivel_actual]
        self.cell_size = 18

    def draw(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                if cell == 1:
                    pyxel.blt(screen_x, screen_y, 1, 0, 0, 17, 17, 0)
                elif cell == 2:
                    pyxel.circ(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 2, 7)

    def update(self, pacman):
        """
        Cambia de nivel si Pacman alcanza la puntuación requerida.
        """
        if pacman._contador >= 5000:  # Puntuación objetivo para cambiar de nivel
            print(f"Nivel {self.nivel_actual + 1} completado. Cambiando de nivel...")
            self.nivel_actual += 1
            if self.nivel_actual < len(self.niveles):
                self.maze = self.niveles[self.nivel_actual]  # Cambiar al siguiente nivel
                pacman.reset_posicion()  # Reiniciar Pacman
                pacman._contador = 0  # Reiniciar puntuación si es necesario
                print(f"¡Nivel {self.nivel_actual + 1} cargado!")
            else:
                print("¡Juego completado!")
                pyxel.quit()
