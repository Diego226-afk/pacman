import pyxel
import random
class Fanta():
    def __init__(self, map_instance, x, y, color, vel=4):
        self.x = x
        self.y = y
        self.xo = x  # Posición inicial
        self.yo = y  # Posición inicial
        self.color = color
        self.vel = vel
        self.dire = "izq"
        self.sprite_size = 15
        self.timer = 0
        self.map = map_instance
        self._momento = 0
        self._modo = "ataque"  # Modos: ataque, miedo, comido
        self.tiempo_miedo = 0  # Temporizador para el modo miedo

    def update(self, pacman, fantasmas):
        """
        Actualiza el estado del fantasma, controlando su velocidad y comportamiento.
        """
        self.timer += 5
        if self.timer % 15 == 0:  # Control de velocidad
            if self._modo == "ataque":
                if isinstance(self, Inky):  # Inky necesita referencia de Blinky
                    self.comportamiento(pacman, fantasmas[0])  # Blinky como referencia
                else:
                    self.comportamiento(pacman)
            elif self._modo == "miedo":
                self.huir_de(pacman)  # Huir en modo miedo

        # Verificar colisión con Pac-Man
        if self.colision_con_pacman(pacman):
            if self._modo == "ataque":
                pacman.vidas -= 1
                pacman.reset_posicion()
                print(f"Pacman perdió una vida. Vidas restantes: {pacman.vidas}")
                if pacman.vidas <= 0:
                    print("¡Game Over!")
                    pyxel.quit()
                # Reiniciar todos los fantasmas
                for fantasma in fantasmas:
                    fantasma.reset_fantasmas()
            elif self._modo == "miedo":
                print("¡Fantasma comido!")
                pacman.incrementar_puntaje(500)
                self.reset_fantasmas()  # Reiniciar posición del fantasma
                self._modo = "comido"

        # Actualizar temporizador de modo miedo
        if self._modo == "miedo" and pyxel.frame_count > self.tiempo_miedo:
            self.volver_normal()
        
        if pyxel.btn(pyxel.KEY_P):
            self._modo = "miedo"

    def reset_fantasmas(self):
        """ Resetea la posición del fantasma a su posición inicial """
        self.x = self.xo
        self.y = self.yo
        self._modo = "ataque"  # Vuelve al modo ataque

    def huir_de(self, pacman):
        """ Mueve al fantasma lejos de Pacman en el modo miedo """
        dx = self.x - pacman.x
        dy = self.y - pacman.y
        objetivo_x = self.x + (dx // abs(dx) * self.vel if dx != 0 else 0)
        objetivo_y = self.y + (dy // abs(dy) * self.vel if dy != 0 else 0)
        self.mover_hacia_objetivo(objetivo_x, objetivo_y)

    def volver_vulnerable(self):
        """ Cambia el estado del fantasma a miedo """
        self._modo = "miedo"
        self.color = 12  # Cambia el color para indicar vulnerabilidad
        self.tiempo_miedo = pyxel.frame_count + 300  # Dura 300 frames (~5 segundos a 60 FPS)

    def volver_normal(self):
        """ Restaura el estado normal del fantasma """
        self._modo = "ataque"
        self.color = 8  # Restaura el color original

    def ver_colisiones(self, new_x, new_y):
        """ Verifica si la nueva posición está bloqueada por una pared """
        left = (new_x + 3) // self.map.cell_size
        right = (new_x + self.sprite_size - 2) // self.map.cell_size
        top = (new_y + 3) // self.map.cell_size
        bottom = (new_y + self.sprite_size - 2) // self.map.cell_size

        # Validar índices dentro del rango de la matriz
        if (0 <= top < len(self.map.maze) and 
            0 <= bottom < len(self.map.maze) and 
            0 <= left < len(self.map.maze[0]) and 
            0 <= right < len(self.map.maze[0])):
            return any(
                self.map.maze[row][col] in (1, 4, 5) 
                for row, col in [(top, left), (top, right), (bottom, left), (bottom, right)]
            )
        return True  # Asumir colisión si está fuera de los límites
    
    def mover_hacia_objetivo(self, objetivo_x, objetivo_y):
        """ Mueve al fantasma hacia un objetivo (objetivo_x, objetivo_y) """
        movimientos = {
            "izq": (self.x - self.vel, self.y),
            "der": (self.x + self.vel, self.y),
            "arr": (self.x, self.y - self.vel),
            "abj": (self.x, self.y + self.vel),
        }

        opciones = []
        for dire, (nx, ny) in movimientos.items():
            if (0 <= nx < len(self.map.maze[0]) * self.map.cell_size and
                0 <= ny < len(self.map.maze) * self.map.cell_size and
                not self.ver_colisiones(nx, ny)):
                opciones.append((dire, nx, ny))

        if not opciones:
            return

        movimientos_opuestos = {"izq": "der", "der": "izq", "arr": "abj", "abj": "arr"}
        if self.dire in movimientos_opuestos:
            opciones = [op for op in opciones if op[0] != movimientos_opuestos[self.dire]]

        if not opciones:
            return

        mejor_opcion = min(opciones, key=lambda o: ((o[1] - objetivo_x) ** 2 + (o[2] - objetivo_y) ** 2))
        self.dire = mejor_opcion[0]
        self.x, self.y = mejor_opcion[1], mejor_opcion[2]
     
    def colision_con_pacman(self, pacman):
        """ Verifica si el fantasma colisiona con Pac-Man """
        return (
            abs(self.x - pacman.x) < self.sprite_size and
            abs(self.y - pacman.y) < self.sprite_size
        )

class Blinky(Fanta):
    def comportamiento(self, pacman):
        """
        Blinky sigue directamente a Pac-Man.
        """
        self.mover_hacia_objetivo(pacman.x, pacman.y)
    def draw(self):
        if self._modo == "miedo":
            pyxel.blt(self.x, self.y, 2, 0, 128, 16, 16, 0)  # Sprite de miedo
        elif self.dire == "der":
            pyxel.blt(self.x, self.y, 2, 32, 0, 16, 16, 0)  # Cambiar las coordenadas del sprite según diseño
        elif self.dire == "izq":
            pyxel.blt(self.x, self.y, 2, 0, 0, 16, 16, 0)
        elif self.dire == "arr":
            pyxel.blt(self.x, self.y, 2, 0, 16, 16, 16, 0)
        elif self.dire == "abj":
            pyxel.blt(self.x, self.y, 2, 32, 16, 16, 16, 0)
             

class Pinky(Fanta):
    def comportamiento(self, pacman):
        """
        Pinky anticipa el movimiento de Pac-Man.
        """
        objetivo_x, objetivo_y = pacman.x, pacman.y
        if pacman.direccion == "izq":
            objetivo_x -= 4 * 16
        elif pacman.direccion == "der":
            objetivo_x += 4 * 16
        elif pacman.direccion == "arr":
            objetivo_y -= 4 * 16
        elif pacman.direccion == "abj":
            objetivo_y += 4 * 16

        self.mover_hacia_objetivo(objetivo_x, objetivo_y)
    def draw(self):
        if self._modo == "miedo":
            pyxel.blt(self.x, self.y, 2, 0, 128, 16, 16, 0)  # Sprite de miedo
        elif self.dire == "der":
            pyxel.blt(self.x, self.y, 2, 32, 32, 16, 16, 0)  # Cambiar las coordenadas del sprite según diseño
        elif self.dire == "izq":
            pyxel.blt(self.x, self.y, 2, 0, 32, 16, 16, 0)
        elif self.dire == "arr":
            pyxel.blt(self.x, self.y, 2, 0, 48, 16, 16, 0)
        elif self.dire == "abj":
            pyxel.blt(self.x, self.y, 2, 32, 48, 16, 16, 0)


class Inky(Fanta):
    def comportamiento(self, pacman, blinky):
        """
        Inky calcula un objetivo dinámico basado en Blinky y Pac-Man.
        """
        vector_x = (pacman.x - blinky.x) * 2
        vector_y = (pacman.y - blinky.y) * 2
        objetivo_x = blinky.x + vector_x
        objetivo_y = blinky.y + vector_y

        self.mover_hacia_objetivo(objetivo_x, objetivo_y)
    def draw(self):
        if self._modo == "miedo":
            pyxel.blt(self.x, self.y, 2, 0, 128, 16, 16, 0)  # Sprite de miedo
        elif self.dire == "der":
            pyxel.blt(self.x, self.y, 2, 32, 96, 16, 16, 0)  # Cambiar las coordenadas del sprite según diseño
        elif self.dire == "izq":
            pyxel.blt(self.x, self.y, 2, 0, 96, 16, 16, 0)
        elif self.dire == "arr":
            pyxel.blt(self.x, self.y, 2, 0, 112, 16, 16, 0)
        elif self.dire == "abj":
            pyxel.blt(self.x, self.y, 2, 32, 112, 16, 16, 0)

class Clyde(Fanta):
    def comportamiento(self, pacman):
        """
        Clyde alterna entre seguir a Pac-Man y deambular aleatoriamente.
        """
        distancia = ((self.x - pacman.x) ** 2 + (self.y - pacman.y) ** 2) ** 0.5
        if distancia > 8 * 16:
            self.mover_hacia_objetivo(pacman.x, pacman.y)
        else:
            direcciones = {"izq": (-self.vel, 0), "der": (self.vel, 0),
                           "arr": (0, -self.vel), "abj": (0, self.vel)}
            self.dire = random.choice(list(direcciones.keys()))
            new_x, new_y = self.x + direcciones[self.dire][0], self.y + direcciones[self.dire][1]
            if not self.ver_colisiones(new_x, new_y):
                self.x, self.y = new_x, new_y
    def draw(self):
        if self._modo == "miedo":
            pyxel.blt(self.x, self.y, 2, 0, 128, 16, 16, 0)  # Sprite de miedo
        elif self.dire == "der":
            pyxel.blt(self.x, self.y, 2, 32, 64, 16, 16, 0)  # Cambiar las coordenadas del sprite según diseño
        elif self.dire == "izq":
            pyxel.blt(self.x, self.y, 2, 0, 64, 16, 16, 0)
        elif self.dire == "arr":
            pyxel.blt(self.x, self.y, 2, 0, 80, 16, 16, 0)
        elif self.dire == "abj":
            pyxel.blt(self.x, self.y, 2, 32, 80, 16, 16, 0)

  



    



    
    




    


        