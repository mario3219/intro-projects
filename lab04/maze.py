import math
import os
import turtle
import tkinter as tk

class Maze:
    def __init__(self, maze_num):
        self._window_width = 420
        self._window_height = 400

        # Make filename relative to the script's directory
        filename = f"images/maze{maze_num}.gif"
        self._img_path = os.path.join(os.path.dirname(__file__), filename)

        # Set entry position
        if maze_num >= 1 and maze_num <= 3:
            self._entry = (105, 203)
        elif maze_num == 4:
            self._entry = (165, 323)
        elif maze_num == 5:
            self._entry = (162, 320)
        else:
            raise Exception("The value of maze_num must be between 1 and 5")

        self._init_screen()
        self._init_maze()

    def _init_screen(self):
        screen = turtle.Screen()
        screen.setup(self._window_width, self._window_height)
        screen.cv._rootwindow.resizable(False, False)
        screen.bgpic(self._img_path)

    def _init_maze(self):
        # Read image and treat pixels that are white or transparent as non-walls.
        # Build boolean list-of-lists representing which pixels correspond to walls.
        img = tk.PhotoImage(file=self._img_path)
        self._walls = []
        for x in range(img.width()):
            row = []
            for y in range(img.height()):
                r, g, b = img.get(x, y)
                is_white = r == 255 and g == 255 and b == 255
                is_transparent = img.transparency_get(x, y)
                is_wall = not(is_white or is_transparent)
                row.append(is_wall)
            self._walls.append(row)

    # The window/turtle and image have different coordinate systems:
    # - The window has origin in the center and y grows upwards.
    # - The image has origin in the top left corner and y grows downwards.
    # The parameters in public methods use the window coordinate system.
    # The following two methods translate between the two coordinate systems.
    def _to_image_coordinate_system(self, pos):
        return (pos[0] + len(self._walls)//2,
                len(self._walls[0])//2 - pos[1])

    def _to_window_coordinate_system(self, pos):
        return (pos[0] - len(self._walls)//2,
                len(self._walls[0])//2 - pos[1])

    def _wall_in(self, direction, pos):
        x, y = self._to_image_coordinate_system(pos)

        next_x = round(x + math.cos(math.radians(direction)))
        next_y = round(y - math.sin(math.radians(direction)))

        # Check if there is any wall among the pixels one step forward
        for x in range(max(0, next_x-1), min(len(self._walls), next_x+2)):
            for y in range(max(0, next_y-1), min(len(self._walls[0]), next_y+2)):
                if self._walls[x][y]:
                    return True
        return False

    #
    # Public methods
    #
    def wall_in_front(self, direction, pos):
        return self._wall_in(direction, pos)

    def wall_at_left(self, direction, pos):
        return self._wall_in(direction+90, pos)

    def at_exit(self, pos):
        _, y = self._to_image_coordinate_system(pos)
        return y <= 0

    def entry(self):
        return self._to_window_coordinate_system(self._entry)