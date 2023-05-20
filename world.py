import numpy as np


class World:
    _R = np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
    grid = [[0 for _ in range(11)] for _ in range(11)]
    origin = 5

    def __init__(self, *items):
        self.items = []
        for item in items:
            self.add_item(item)
            self.items.append(item)

    def add_item(self, v=(0, 0, 0)):
        x, y, theta = v
        x, y = x + self.origin, -y + self.origin
        self.grid[y][x] = 1

    def __str__(self):
        newline = "\n"  # \escapes are not allowed inside f-strings
        world = f'{newline.join(f"{self.grid[count]}" for count, _ in enumerate(self.grid))}'
        return world


if __name__ == "__main__":
    world = World()
    world.add_item((-2, 2, 0))
    print(world)
