import pyxel

class PacmanGame:
    def __init__(self):
        self.width = 160
        self.height = 120
        self.cell_size = 8
        pyxel.init(self.width, self.height)  # Elimina el argumento caption
        pyxel.title = "Pac-Man"  # Opcional para versiones antiguas
        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                if cell == 1:  # Dibuja paredes
                    pyxel.images[0].load(0, 0, "boca-abierta.png")(screen_x, screen_y, self.cell_size, self.cell_size, 9)
                elif cell == 2:  # Dibuja puntos pequeños
                    pyxel.circ(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 2, 7)

PacmanGame()
