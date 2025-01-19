import pyxel
from bolas import Punto
from muros import Bloque
import random

class Map:
    def __init__(self, niveles):
        self.niveles = niveles  # Lista de niveles
        self.nivel_actual = 0  # Empieza en el primer nivel
        self.cell_size = 18
        self.listaPuntos = []
        self.listaBloques = []
        self.puntos_nivel = 0  # Inicializa a 0
        self.inicializar_nivel()  # Carga el primer nivel
     

    def inicializar_nivel(self):
        """
        Inicializa el nivel actual cargando bloques y puntos.
        """
        print(f"Iniciando nivel {self.nivel_actual + 1}...")
        if self.nivel_actual >= len(self.niveles):
            print("¡No hay más niveles disponibles!")
            pyxel.quit()

        self.listaBloques = []
        self.listaPuntos = []
        self.listaGpuntos = []
        self.listaBloques2 = []
        self.listaBloques3 = []
        self.puntos_nivel = 0  # Reinicia el conteo de puntos

        self.maze = self.niveles[self.nivel_actual]  # Carga el nivel actual

        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                if cell == 1:  # Bloques
                    self.listaBloques.append(Bloque(screen_x, screen_y))
                elif cell == 2:  # Puntos
                    self.listaPuntos.append(Punto(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 2, 7))
                    self.puntos_nivel += 1  # Incrementa los puntos del nivel
                elif cell == 3:  # Puntos grandes
                    self.listaGpuntos.append(Punto(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 4, 7))
                elif cell == 4:  # Segundos bloques
                    self.listaBloques2.append(Bloque(screen_x, screen_y))
                elif cell == 5:  # Terceros bloques
                    self.listaBloques3.append(Bloque(screen_x, screen_y))

        # Añadir fruta encima de un punto aleatorio
        if len(self.listaPuntos) > 0:  # Asegurarse de que hay puntos en el mapa
            punto_aleatorio = random.choice(self.listaPuntos)
            # Cambiar el tipo del punto a "fruta"
            punto_aleatorio.tipo = "fruta"


    def update(self, pacman, listaFantasmas):
        """
        Cambia de nivel si Pacman alcanza la puntuación necesaria,
        y gestiona la recogida de bolas de poder.
        """
        if pacman._marcador >= self.puntos_nivel:  # Puntuación objetivo para cambiar de nivel
            print(f"Nivel {self.nivel_actual + 1} completado. Cambiando de nivel...")
            self.nivel_actual += 1
            if self.nivel_actual < len(self.niveles):
                pacman.reset_posicion()  # Reiniciar la posición de Pacman
                pacman._marcador = 0  # Reiniciar marcador
                self.inicializar_nivel()  # Inicializar el nuevo nivel
                for fantasma in listaFantasmas:
                    fantasma.reset_fantasmas()
                print(f"¡Nivel {self.nivel_actual + 1} cargado!")
            else:
                print("¡Juego completado!")
                pyxel.quit()


    def draw(self):
        """
        Dibuja los puntos, bloques y bolas de poder en pantalla.
        """
        # Dibujar puntos normales
        for punto in self.listaPuntos:
            if getattr(punto, "tipo", None) == "fruta":  # Si es una fruta
                # Dibujar fruta con pyxel.blt
                pyxel.blt(punto.x - 8, punto.y - 8, 1, 32, 40, 16, 16, 0)  # Sprite de la fruta
            else:
                # Dibujar puntos normales
                pyxel.circ(punto.x, punto.y, punto.r, punto.col)

        # Dibujar bloques
        for bloque in self.listaBloques:
            pyxel.blt(bloque.x, bloque.y, 1, 0, 0, 17, 17, 0)

        for bloque2 in self.listaBloques2:
            pyxel.blt(bloque2.x, bloque2.y, 1, 24, 0, 17, 17, 0)
        
        for bloque3 in self.listaBloques3:
            pyxel.blt(bloque3.x, bloque3.y, 1, 48, 0, 17, 17, 0)
        
        # Dibujar puntos grandes 
        for punto in self.listaGpuntos:
            pyxel.circ(punto.x, punto.y, 6, 10)  # Bola de poder con radio 6 y color 10
