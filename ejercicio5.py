#Ejercicio 5

class Pacman:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._puntaje = 0
        self._has_power = False
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def puntaje(self):
        return self._puntaje

    def añadir_puntaje(self, puntos):
        self._puntaje += puntos

    @property
    def potenciado(self):
        return self.potenciado

    @potenciado.setter
    def potenciado(self, value):
        self._potenciado = value

class Fantasma:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color
        self._miedo = False

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def color(self):
        return self._color

    @property
    def miedo(self):
        return self._miedo

    @miedo.setter
    def miedo(self, value):
        self._miedo = value

class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._comido = False

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def comido(self):
        return self._comido

    def comer(self):
        self._comido = True

class BolaPoder(Punto):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._comido = False

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def comido(self):
        return self._comido

    def comer(self):
        self._comido = True
        return "Puedes comerte a los fantasmas"
    