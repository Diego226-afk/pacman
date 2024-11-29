import pyxel
from Mapas import Map
class Pacman:
    def __init__(self, map_instance):
        self.x = 18
        self.y = 18
        self.velocidad = 2
        self.direccion = "derecha"
        self.base = 1
        self.map = map_instance  # Pasar la instancia del mapa
        self.sprite_size = 14  # Tamaño del sprite
        self._momento = 0
        self._contador = 0

    def update(self):
        next_x, next_y = self.x, self.y

        # Mover hacia la izquierda
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            next_x -= self.velocidad
            self.direccion = "izquierda"
            self.base = -1

        # Mover hacia la derecha
        elif (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            next_x += self.velocidad
            self.direccion = "derecha"
            self.base = 1

        # Mover hacia arriba
        elif (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
            next_y -= self.velocidad
            self.direccion = "arriba"
            self.base = -1

        # Mover hacia abajo
        elif (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
            next_y += self.velocidad
            self.direccion = "abajo"

        # Comprobar colisión antes de actualizar la posición
        if not self.ver_colisiones(next_x, next_y):
            self.x, self.y = next_x, next_y
        
        

        self.ñam_bolas(self.x , self.y)
        self.tp()

    def ver_colisiones(self, new_x, new_y):
        # Calcular las coordenadas de la celda en la matriz del mapa
        left = (new_x + 3) // self.map.cell_size
        right = (new_x + self.sprite_size - 1) // self.map.cell_size
        top = (new_y + 3) // self.map.cell_size
        bottom = (new_y + self.sprite_size - 1) // self.map.cell_size

        # Verificar si alguna esquina de Pacman está dentro de un muro
        return (
            self.map.maze[top][left] == 1 or
            self.map.maze[top][right] == 1 or
            self.map.maze[bottom][left] == 1 or
            self.map.maze[bottom][right] == 1
        )
    

    def tp(self):
        if self.x<=0:
            self.x = 35*18
            self.y = 9*18
        elif self.x>=35*18:
            self.x = 0
            self.y = 9*18
    
    def ñam_bolas(self, new_x, new_y):
            cell_x = new_x // self.map.cell_size
            cell_y = new_y // self.map.cell_size

            if self.map.maze[cell_y][cell_x] == 2:
                self.map.maze[cell_y][cell_x] = 0 
                self._contador+=200
                return True  
            return False
    

    def draw(self):
          # Limpiar la pantalla
        pyxel.text(10, 10, f"{self._contador} puntos", 8)
        self._momento+=1
        if self._momento==32:
            self._momento=0
        if self._momento<8:
            if self.direccion=="derecha":
                pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)
            if self.direccion=="izquierda":
                pyxel.blt(self.x, self.y, 0, 0, 32, 16, 16, 0)
            if self.direccion=="arriba":
                pyxel.blt(self.x, self.y, 0, 32, 16, 16, 16, 0)
            if self.direccion=="abajo":
                pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, 0)
                
        if self._momento>=8:
            if self.direccion=="derecha":
                pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
            if self.direccion=="izquierda":
                pyxel.blt(self.x, self.y, 0, 16, 32, 16, 16, 0)
            if self.direccion=="abajo":
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16, 0)
            if self.direccion=="arriba":
                pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16, 0)
