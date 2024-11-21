import pyxel

class Pacman:
    def __init__(self, x, y):
        
        pyxel.init(256, 256, title="Pacman")  
        
        self.x = x  
        self.y = y  
        self.velocidad = 5  
        self.direccion = "derecha"
        pyxel.images[0].load(0, 0, "boca-abierta.png")
        pyxel.images[1].load(0, 0, "boca-cerrada.png")

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.velocidad
            self.direccion = "izquierda"
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.velocidad
            self.direccion = "derecha"
        if pyxel.btn(pyxel.KEY_W):
            self.y -= self.velocidad
            self.direccion = "arriba"
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.velocidad
            self.direccion = "abajo"

    def draw(self):
        pyxel.cls(0)

        if self.direccion == "derecha":
            pyxel.blt(self.x, self.y, 0, 0, 0, 17, 17, 0)
        elif self.direccion == "izquierda":
            pyxel.blt(self.x, self.y, 1, 0, 0, 17, 17, 0)  
        elif self.direccion == "arriba":
            pyxel.blt(self.x, self.y, 0, 0, 0, 17, 17, 0)  
        elif self.direccion == "abajo":
            pyxel.blt(self.x, self.y, 1, 0, 0, 17, 17, 0) 
            
player = Pacman(128, 128)
Pacman()
