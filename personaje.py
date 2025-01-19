class Personaje:
    def __init__(self, map_instance):
        self.map = map_instance 

    def ver_colisiones(self, new_x, new_y):
            left = (new_x + 3) // self.map.cell_size
            right = (new_x + self.sprite_size - 2) // self.map.cell_size
            top = (new_y + 3) // self.map.cell_size
            bottom = (new_y + self.sprite_size - 2) // self.map.cell_size

            return (
                self.map.maze[top][left] == 1 or
                self.map.maze[top][right] == 1 or
                self.map.maze[bottom][left] == 1 or
                self.map.maze[bottom][right] == 1
            )