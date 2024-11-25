import pyxel

# Initialize Pyxel at the beginning of the program
pyxel.init(340, 170, title="Pacman", fps=60)

class Pacman:
    def __init__(self, map_instance):
        pyxel.load("pacman.pyxres")  # Assuming this contains Pac-Man sprite
        self.x = 128
        self.y = 128
        self.velocidad = 2
        self.direccion = "derecha"
        self.base = 1
        self.map = map_instance  # Pass map instance to Pacman
        pyxel.run(self.update, self.draw)

    def update(self):
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)) and (self.x - self.velocidad >= 0):
            self.x -= self.velocidad
            self.direccion = "izquierda"
            self.base = -1
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)) and (self.x + self.velocidad <= pyxel.width - 15):
            self.x += self.velocidad
            self.direccion = "derecha"
            self.base = 1
        if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and (self.y - self.velocidad >= 0):
            self.y -= self.velocidad
            self.direccion = "arriba"
        if (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)) and (self.y + self.velocidad <= pyxel.height - 16):
            self.y += self.velocidad
            self.direccion = "abajo"

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        pyxel.blt(self.x, self.y, 0, 0, 0, self.base * 16, 17, 0)
            

class Map:
    def __init__(self):
        # Map initialization
        self.width = 340
        self.height = 270
        self.cell_size = 17
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

    def draw(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                if cell == 1:  # Draw walls
                    pyxel.blt(screen_x, screen_y, 1, 0, 0, 17, 17, 0) 
                elif cell == 2:  # Draw small dots
                    pyxel.circ(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 2, 7) 


map_instance = Map()
Pacman(map_instance)



