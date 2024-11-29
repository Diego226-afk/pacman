import pyxel, random
from Mapas import Pacman

class Fanta(Pacman):
    def __init__(self, pos_x, pos_y, map_instance):
        self.x = pos_x
        self.y = pos_y
        self.velocidad = 1  # Los fantasmas se mueven más lento que Pacman
        self.map = map_instance  # Reutilizamos el mapa de la clase Pacman
        self.direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
        self.sprite_size = 14

    def update(self):
        # Movimiento aleatorio básico
        dx, dy = 0, 0
        if self.direccion == "izquierda":
            dx = -self.velocidad
        elif self.direccion == "derecha":
            dx = self.velocidad
        elif self.direccion == "arriba":
            dy = -self.velocidad
        elif self.direccion == "abajo":
            dy = self.velocidad

        next_x, next_y = self.x + dx, self.y + dy

        # Cambiar de dirección si hay colisión
        if self.ver_colisiones(next_x, next_y):
            self.direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
        else:
            self.x, self.y = next_x, next_y

    def draw(self):
        # Dibujar al fantasma
        pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)  # Cambiar las coordenadas de sprites si es necesario

    def coli_pac(self, pacman_x, pacman_y):
        # Comprobar si colisiona con Pacman
        if abs(self.x - pacman_x) < self.sprite_size and abs(self.y - pacman_y) < self.sprite_size:
            print("¡Pac-Man ha sido atrapado!")

class Naranja(Fanta):
    def __init__(self, pos_x, pos_y, map_instance):
        super().__init__(pos_x, pos_y, map_instance)
        self.color = "naranja"




    


        