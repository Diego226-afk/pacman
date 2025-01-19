import pyxel

class Pacman():
    def __init__(self, map_instance, fantasmas):
        self.map = map_instance 
        self.map_instance = map_instance
        self.fantasmas = fantasmas
        self.x = 18
        self.y = 18
        self.velocidad = 2
        self.direccion = "derecha"
        self.sprite_size = 15
        self._contador = 0
        self._momento = 0
        self._moviendo = False  # Inicializamos _moviendo
        self.vidas = 3
        self._marcador = 0
        self.modo_poder = False  # Indica si está en modo de poder
        self.tiempo_poder = 0  # Temporizador para el modo de poder

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
        self.comer_Gbolas()

        if self.modo_poder:
            self.actualizar_modo_poder()

    def ver_colisiones(self, new_x, new_y):
        left = (new_x + 3) // self.map.cell_size
        right = (new_x + self.sprite_size - 2) // self.map.cell_size
        top = (new_y + 3) // self.map.cell_size
        bottom = (new_y + self.sprite_size - 2) // self.map.cell_size

        return any(
            self.map.maze[row][col] in (1, 4, 5) 
            for row, col in [(top, left), (top, right), (bottom, left), (bottom, right)]
        )

    def tp(self):
        if self.x <= 0:
            self.x = 35 * 18
            self.y = 9 * 18
        elif self.x >= 35 * 18:
            self.x = 0
            self.y = 9 * 18

    def comer_bolas(self):
        for punto in self.map_instance.listaPuntos[:]:
            pacman_rect = (self.x, self.y, self.x + self.sprite_size, self.y + self.sprite_size)
            punto_rect = (punto.x - punto.r, punto.y - punto.r, punto.x + punto.r, punto.y + punto.r)

            if self._rect_collision(pacman_rect, punto_rect):
                self.incrementar_puntaje(100)
                self._marcador += 1
                self.map_instance.listaPuntos.remove(punto)
                break
    
    def comer_Gbolas(self):
        for punto in self.map_instance.listaGpuntos[:]:
            pacman_rect = (self.x, self.y, self.x + self.sprite_size, self.y + self.sprite_size)
            punto_rect = (punto.x - punto.r, punto.y - punto.r, punto.x + punto.r, punto.y + punto.r)

            if self._rect_collision(pacman_rect, punto_rect):
                self.incrementar_puntaje(500)
                self.map_instance.listaGpuntos.remove(punto)
                self.activar_modo_poder()  # Activar modo de poder
                break
    
    def activar_modo_poder(self):
        """
        Activa el modo de poder para Pacman.
        """
        print("¡Modo de poder activado!")
        self.modo_poder = True
        self.tiempo_poder = 0
        self.tiempo_poder = pyxel.frame_count + 300  # Dura 300 frames (~5 segundos a 60 FPS)

        # Hacer a los fantasmas vulnerables
        for fantasma in self.fantasmas:
            fantasma.volver_vulnerable()

    def actualizar_modo_poder(self):
        """
        Actualiza el temporizador del modo de poder y descativa si se acaba.
        """
        if pyxel.frame_count >= self.tiempo_poder:
            print("El modo de poder ha terminado.")
            self.modo_poder = False
            for fantasma in self.fantasmas:
                fantasma.volver_normal()
    
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
        pyxel.text(72, 18, f"Vidas: {self.vidas}", 8)
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
