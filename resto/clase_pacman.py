import pyxel

class Pacman:
    def __init__(self):
        
        pyxel.init(256, 256, title="Pacman")  
        self.x = 0  
        self.y = 0  

        self.direccion = "derecha"
        pyxel.images[0].load(0, 0, "boca-abierta.png")
        pyxel.images[1].load(0, 0, "boca-cerrada.png")

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
            self.direccion = "izquierda"
        if pyxel.btn(pyxel.KEY_D):
            self.x += 2
            self.direccion = "derecha"
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
            self.direccion = "arriba"
        if pyxel.btn(pyxel.KEY_S):
            self.y += 2
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
            
Pacman()
