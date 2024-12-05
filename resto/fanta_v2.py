import random
import pyxel

class Fantasma:
    def __init__(self, x, y, color_offset, map_instance):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.sprite_size = 15
        self.direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
        self.color_offset = color_offset  # Offset para seleccionar sprite de color específico
        self.map = map_instance

    def update(self, map_instance, pacman_x, pacman_y):
        """Lógica genérica para actualizar la posición, cambiar dirección si es necesario."""
        if random.randint(0, 20) == 0:  # Cambiar dirección aleatoriamente
            self.direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])

        next_x, next_y = self.x, self.y
        if self.direccion == "izquierda":
            next_x -= self.velocidad
        elif self.direccion == "derecha":
            next_x += self.velocidad
        elif self.direccion == "arriba":
            next_y -= self.velocidad
        elif self.direccion == "abajo":
            next_y += self.velocidad

        # Comprobar colisiones antes de mover
        if not self.ver_colisiones(next_x, next_y, map_instance):
            self.x, self.y = next_x, next_y

        # Teletransportarse si salen del mapa
        self.tp(map_instance)

    def ver_colisiones(self, new_x, new_y, map_instance):
        """Verificar si el fantasma colisiona con las paredes del mapa."""
        left = (new_x + 3) // map_instance.cell_size
        right = (new_x + self.sprite_size - 2) // map_instance.cell_size
        top = (new_y + 3) // map_instance.cell_size
        bottom = (new_y + self.sprite_size - 2) // map_instance.cell_size

        return (
            map_instance.maze[top][left] == 1 or
            map_instance.maze[top][right] == 1 or
            map_instance.maze[bottom][left] == 1 or
            map_instance.maze[bottom][right] == 1
        )

    def tp(self, map_instance):
        """Reutilizamos la lógica de teletransportación del Pacman."""
        if self.x <= 0:
            self.x = 35 * map_instance.cell_size
        elif self.x >= 35 * map_instance.cell_size:
            self.x = 0

    def draw(self):
        """
        Dibuja al fantasma en la posición actual.
        """
        pyxel.blt(self.x, self.y, 0, self.color_offset, 0, 16, 16, 0)  # Usa el sprite desde la hoja de recursos


class Blinky(Fantasma):
    def draw(self):
        """
        Dibuja al fantasma en la posición actual.
        """
        pyxel.blt(self.x, self.y, 0, self.color_offset, 0, 16, 16, 0)  # Usa el sprite desde la hoja de recursos

    def __init__(self, x, y, color_offset, map_instance):
        super().__init__(x, y, color_offset, map_instance)  # Inicializar clase base
    def update(self, map_instance, pacman_x, pacman_y):
        """Perseguir a Pacman directamente."""
        if abs(self.x - pacman_x) > abs(self.y - pacman_y):
            self.direccion = "izquierda" if self.x > pacman_x else "derecha"
        else:
            self.direccion = "arriba" if self.y > pacman_y else "abajo"
        super().update(map_instance, pacman_x, pacman_y)

class Pinky(Fantasma):
    def __init__(self, x, y, color_offset, map_instance):
        super().__init__(x, y, color_offset, map_instance)  # Inicializar clase base
    def update(self, map_instance, pacman_x, pacman_y):
        """Intentar anticipar movimientos de Pacman (4 pasos adelante)."""
        if abs(self.x - pacman_x) > abs(self.y - pacman_y):
            self.direccion = "izquierda" if self.x > pacman_x - 4 * self.velocidad else "derecha"
        else:
            self.direccion = "arriba" if self.y > pacman_y - 4 * self.velocidad else "abajo"
        super().update(map_instance, pacman_x, pacman_y)

class Inky(Fantasma):
    def __init__(self, x, y, color_offset, map_instance):
        super().__init__(x, y, color_offset, map_instance)  # Inicializar clase base
    def update(self, map_instance, pacman_x, pacman_y, blinky_x, blinky_y):
        """Usar un punto entre Pacman y Blinky para calcular dirección."""
        target_x = 2 * pacman_x - blinky_x
        target_y = 2 * pacman_y - blinky_y
        if abs(self.x - target_x) > abs(self.y - target_y):
            self.direccion = "izquierda" if self.x > target_x else "derecha"
        else:
            self.direccion = "arriba" if self.y > target_y else "abajo"
        super().update(map_instance, pacman_x, pacman_y)

class Clyde(Fantasma):
    def __init__(self, x, y, color_offset, map_instance):
        super().__init__(x, y, color_offset, map_instance)  # Inicializar clase base
    def update(self, map_instance, pacman_x, pacman_y):
        """Alternar entre perseguir a Pacman y alejarse."""
        distance = ((self.x - pacman_x) ** 2 + (self.y - pacman_y) ** 2) ** 0.5
        if distance > 100:  # Perseguir si está lejos
            if abs(self.x - pacman_x) > abs(self.y - pacman_y):
                self.direccion = "izquierda" if self.x > pacman_x else "derecha"
            else:
                self.direccion = "arriba" if self.y > pacman_y else "abajo"
        else:  # Alejarse si está cerca
            self.direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
        super().update(map_instance, pacman_x, pacman_y)

