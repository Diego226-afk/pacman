import pyxel
from pacman import Pacman as pc

class Fanta(pc):
    def __init__(self, x, y, color, vel=2):
        self.x = x
        self.y = y
        self.color = color
        self.vel = vel
        self.dire = "izq"

    def update(self):
        self.tp()
        self.ver_colisiones()

    def tocar(self):
        # Verifica si el fantasma ha tocado a Pac-Man
        if self.x == pc.x and self.y == pc.y:
            return True

    def tp(self):
        super().tp()

    def ver_colisiones(self):
        super().ver_colisiones()

    def mover_hacia_objetivo(self, objetivo_x, objetivo_y):
        """
        Mueve al fantasma hacia un punto objetivo (objetivo_x, objetivo_y).
        """
        if self.x < objetivo_x:
            self.dire = "der"
            self.x += self.vel
        elif self.x > objetivo_x:
            self.dire = "izq"
            self.x -= self.vel
        if self.y < objetivo_y:
            self.dire = "abj"
            self.y += self.vel
        elif self.y > objetivo_y:
            self.dire = "arr"
            self.y -= self.vel

    def draw(self):
        """
        Dibuja al fantasma basado en su dirección y color.
        """
        direcciones = {
            "izq": 0,
            "der": 1,
            "arr": 2,
            "abj": 3
        }
        columna = direcciones[self.dire] * 16
        fila = self.color * 16

        # Dibuja el fantasma
        pyxel.blt(self.x, self.y, 2, columna, fila, 16, 16, 0)


class Blinky(Fanta):
    def comportamiento(self, pacman):
        """Sigue directamente a Pac-Man"""
        self.mover_hacia_objetivo(pacman.x, pacman.y)

class Pinky(Fanta):
    def comportamiento(self, pacman):
        """Anticipa el movimiento de Pac-Man"""
        objetivo_x = pacman.x
        objetivo_y = pacman.y
        if pacman.direccion == "izq":
            objetivo_x = pacman.x - 4 * 16
            objetivo_y = pacman.y
        elif pacman.direccion == "der":
            objetivo_x = pacman.x + 4 * 16
            objetivo_y = pacman.y
        elif pacman.direccion == "arr":
            objetivo_x = pacman.x
            objetivo_y = pacman.y - 4 * 16
        elif pacman.direccion == "abj":
            objetivo_x = pacman.x
            objetivo_y = pacman.y + 4 * 16

        self.mover_hacia_objetivo(objetivo_x, objetivo_y)

class Inky(Fanta):
    def comportamiento(self, pacman, blinky):
        """Calcula un objetivo dinámico basado en Blinky y Pac-Man"""
        vector_x = (pacman.x - blinky.x) * 2
        vector_y = (pacman.y - blinky.y) * 2
        objetivo_x = blinky.x + vector_x
        objetivo_y = blinky.y + vector_y
        self.mover_hacia_objetivo(objetivo_x, objetivo_y)

class Clyde(Fanta):
    def comportamiento(self, pacman):
        """Cambia entre seguir a Pac-Man o deambular según la distancia"""
        distancia = ((self.x - pacman.x) ** 2 + (self.y - pacman.y) ** 2) ** 0.5
        if distancia > 8 * 16:  # Si está lejos de Pac-Man, lo sigue
            self.mover_hacia_objetivo(pacman.x, pacman.y)
        else:  # Si está cerca, deambula aleatoriamente
            import random
            self.dire = random.choice(["izq", "der", "arr", "abj"])
            if self.dire == "izq":
                self.x -= self.vel
            elif self.dire == "der":
                self.x += self.vel
            elif self.dire == "arr":
                self.y -= self.vel
            elif self.dire == "abj":
                self.y += self.vel

  



    



    
    




    


        