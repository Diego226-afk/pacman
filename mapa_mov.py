import pyxel

# Inicialización de Pyxel al principio del programa
pyxel.init(340, 170, title="Pacman", fps=60)

class Pacman:
    def __init__(self, map_instance):
        pyxel.load("pacman.pyxres")  # Suponiendo que contiene el sprite de Pac-Man
        self.x = 17
        self.y = 17
        self.velocidad = 2
        self.direccion = "derecha"
        self.base = 1
        self.map = map_instance  # Pasar la instancia del mapa a Pacman
        pyxel.run(self.update, self.draw)

    # Actualiza las posiciones de Pac-Man con las teclas
    def update(self):
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)) and (self.x - self.velocidad >= 0):
            if self.p_paso(self.x - self.velocidad , self.y):
                self.x -= self.velocidad
                self.direccion = "izquierda"
                self.base = -1
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)) and (self.x + self.velocidad <= pyxel.width - 15):
            if self.p_paso(self.x + self.velocidad , self.y):
                self.x += self.velocidad
                self.direccion = "derecha"
                self.base = 1
        if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and (self.y - self.velocidad >= 0):
            if self.p_paso(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
                self.direccion = "arriba"
        if (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)) and (self.y + self.velocidad <= pyxel.height - 16):
            if self.p_paso(self.x, self.y + self.velocidad ):
                self.y += self.velocidad
                self.direccion = "abajo"


    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        pyxel.blt(self.x, self.y, 0, 0, 0, self.base * 16, 17, 0)
    
    
    def p_paso(self, n_x, n_y):
        # Calcula la celda correspondiente en el mapa para la posición de Pac-Man
        if self.direccion=="izquierda":
            casillax = (n_x) // self.map.cell_size  # Desplazar para considerar el tamaño de Pac-Man
            casillay = n_y // self.map.cell_size  # Sin desplazamiento vertical
        elif self.direccion=="derecha":
            casillax = (n_x + 16) // self.map.cell_size  
            casillay = n_y // self.map.cell_size
        elif self.direccion=="arriba":
            casillax = (n_x) // self.map.cell_size  
            casillay = n_y // self.map.cell_size
        elif self.direccion=="abajo":
            casillax = (n_x) // self.map.cell_size  
            casillay = n_y+16 // self.map.cell_size

        

        # Verifica si hay una pared en la celda correspondiente
        if self.map.mapa[casillay][casillax] == 1:
            return False  # No puede pasar (hay una pared)
        return True  # Puede pasar (no hay pared)



        

class Map:
    def __init__(self):
        # Inicialización del mapa
        self.width = 340
        self.height = 270
        self.cell_size = 17
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def draw(self):
        for y, row in enumerate(self.mapa):
            for x, cell in enumerate(row):
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                if cell == 1:  # Dibujar paredes
                    pyxel.blt(screen_x, screen_y, 1, 0, 0, 17, 17, 0) 
                elif cell == 2:  # Dibujar puntos
                    pyxel.circ(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 2, 7) 


mapita = Map()
Pacman(mapita)




