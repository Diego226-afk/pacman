import pyxel

class PacmanGame:
    def __init__(self):
        pyxel.init(1000, 1000)  
        pyxel.title = "Pac-Man" 

        pyxel.images[0].load(0, 0, "boca-abierta.png")
        pyxel.images[1].load(0, 0, "pacman.pyxres")

        self.pacman_x = 0
        self.pacman_y = 0
        self.direction = "derecha"
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pacman_x += 2
            self.direction = "derecha"
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.pacman_x -= 2
            self.direction = "izquierda"
        elif pyxel.btn(pyxel.KEY_UP):
            self.pacman_y -= 2
            self.direction = "arriba"
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.pacman_y += 2
            self.direction = "abajo"

    def draw(self):
        pyxel.cls(1)

        if self.direction == "derecha":
            pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 100, 100, 0)
        elif self.direction == "izquierda":
            pyxel.blt(self.pacman_x, self.pacman_y, 1, 0, 0, 100, 100, 0)
        elif self.direction == "arriba":
            pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 100, 100, 0)
        elif self.direction == "abajo":
            pyxel.blt(self.pacman_x, self.pacman_y, 1, 0, 0, 100, 100, 0)

PacmanGame()
