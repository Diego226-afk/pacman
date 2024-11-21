import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)  
        pyxel.load("azul.pyxres")
        self.x = 0
        self.y = 0
        self.vel=2
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x + 16 < pyxel.width:
            self.x += self.vel 
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= self.vel 
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= self.vel 
        if pyxel.btn(pyxel.KEY_DOWN) and self.y + 16 < pyxel.height:
            self.y += self.vel 

        
        

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, 0, 0, 14, 16, 0)

App()
