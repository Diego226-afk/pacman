import pyxel

class Pacman:
    def __init__(self, map_instance):
        self.x = 18
        self.y = 18
        self.velocidad = 2
        self.direccion = "derecha"
        self.map = map_instance
        self.sprite_size = 15
        self._contador = 0
        self._momento = 0
        self._moviendo = False  # Inicializamos _moviendo

    def update(self):
        next_x, next_y = self.x, self.y
        self._moviendo = False  # Suponemos que no se mueve hasta detectar entrada

        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            next_x -= self.velocidad
            self.direccion = "izquierda"
            self._moviendo = True
        elif pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            next_x += self.velocidad
            self.direccion = "derecha"
            self._moviendo = True
        elif pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
            next_y -= self.velocidad
            self.direccion = "arriba"
            self._moviendo = True
        elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            next_y += self.velocidad
            self.direccion = "abajo"
            self._moviendo = True

        if not self.ver_colisiones(next_x, next_y):
            self.x, self.y = next_x, next_y

        self.tp()
        self.comer_bolas()

    def tp(self):
        if self.x <= 0:
            self.x = 35 * 18
            self.y = 9 * 18
        elif self.x >= 35 * 18:
            self.x = 0
            self.y = 9 * 18

    def ver_colisiones(self, new_x, new_y):
        left = (new_x + 3) // self.map.cell_size
        right = (new_x + self.sprite_size - 2) // self.map.cell_size
        top = (new_y + 3) // self.map.cell_size
        bottom = (new_y + self.sprite_size - 2) // self.map.cell_size

        return (
            self.map.maze[top][left] == 1 or
            self.map.maze[top][right] == 1 or
            self.map.maze[bottom][left] == 1 or
            self.map.maze[bottom][right] == 1
        )

    def comer_bolas(self):
        """
        Detecta y elimina bolas si Pac-Man las toca, utilizando un rectángulo de colisión reducido.
        """
        cell_size = self.map.cell_size

        # Calcula el rectángulo reducido de Pac-Man
        colision_reduccion = 0.3  # Proporción para reducir el tamaño del rectángulo (30% más pequeño)
        reducido_x = self.x + colision_reduccion * cell_size
        reducido_y = self.y + colision_reduccion * cell_size
        reducido_ancho = cell_size * (1 - colision_reduccion * 2)
        reducido_alto = cell_size * (1 - colision_reduccion * 2)

        pacman_rect = (
            reducido_x, reducido_y,
            reducido_x + reducido_ancho, reducido_y + reducido_alto
        )

        # Recorre las celdas vecinas para detectar colisiones
        for dy in range(-1, 2):  # Filas vecinas
            for dx in range(-1, 2):  # Columnas vecinas
                cell_x = (self.x // cell_size) + dx
                cell_y = (self.y // cell_size) + dy

                # Verifica límites del laberinto
                if 0 <= cell_y < len(self.map.maze) and 0 <= cell_x < len(self.map.maze[cell_y]):
                    if self.map.maze[cell_y][cell_x] == 2:  # Si hay una bola
                        # Calcula el rectángulo de la bola
                        bola_rect = (
                            cell_x * cell_size, cell_y * cell_size,
                            (cell_x + 1) * cell_size, (cell_y + 1) * cell_size
                        )

                        # Detecta si los rectángulos se superponen
                        if self._rect_collision(pacman_rect, bola_rect):
                            self.map.maze[cell_y][cell_x] = 0  # Elimina la bola
                            self.incrementar_puntaje(100)      # Incrementa el puntaje

    def _rect_collision(self, rect1, rect2):
        """
        Comprueba si dos rectángulos se superponen.
        """
        x1_min, y1_min, x1_max, y1_max = rect1
        x2_min, y2_min, x2_max, y2_max = rect2

        return not (x1_max <= x2_min or  # Pac-Man a la izquierda de la bola
                    x1_min >= x2_max or  # Pac-Man a la derecha de la bola
                    y1_max <= y2_min or  # Pac-Man encima de la bola
                    y1_min >= y2_max)    # Pac-Man debajo de la bola

    def incrementar_puntaje(self, puntos):
        """
        Incrementa el puntaje del jugador.
        """
        self._contador += puntos

    def reset_posicion(self):
        self.x, self.y = 18, 18

    def draw(self):
        pyxel.text(18, 18, f"{self._contador} puntos", 8)
        self._momento+=1
        if self._momento==32:
            self._momento=0
        if self._momento<8 or not self._moviendo:
            if self.direccion=="derecha":
                pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)
            if self.direccion=="izquierda":
                pyxel.blt(self.x, self.y, 0, 0, 32, 16, 16, 0)
            if self.direccion=="arriba":
                pyxel.blt(self.x, self.y, 0, 32, 16, 16, 16, 0)
            if self.direccion=="abajo":
                pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, 0)
                    
        if self._momento>=8 and self._moviendo:
            if self.direccion=="derecha":
                pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
            if self.direccion=="izquierda":
                pyxel.blt(self.x, self.y, 0, 16, 32, 16, 16, 0)
            if self.direccion=="abajo":
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16, 0)
            if self.direccion=="arriba":
                pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16, 0)
