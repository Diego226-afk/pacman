import pyxel

class Player:
    def __init__(self, x, y):
        self.x = x  # Posición X del jugador
        self.y = y  # Posición Y del jugador
        self.speed = 5  # Velocidad de movimiento

    def update(self):
        # Actualiza la posición del jugador según la entrada del teclado
        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.speed
        if pyxel.btn(pyxel.KEY_W):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.speed

    def draw(self):
        # Dibuja la imagen del jugador en la pantalla
        # Suponiendo que la imagen está en el primer banco (0) y ocupa 16x16 píxeles
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)  # Dibuja la imagen del jugador

def update():
    player.update()  # Actualiza la lógica del jugador

def draw():
    pyxel.cls(0)  # Limpia la pantalla con color negro
    player.draw()  # Dibuja al jugador

# Inicializa la ventana de 256x256 píxeles
pyxel.init(256, 256, title="Mi Juego")  

# Carga el archivo de recursos que contiene la imagen
pyxel.load("my_resource.pyxres")  

# Crea una instancia del jugador en la posición inicial (128, 128)
player = Player(128, 128)

# Inicia el ciclo del juego
pyxel.run(update, draw)  