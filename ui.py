import tkinter as tk
from map import MAP_SIZE

BLOCK_COLOR = ["black", "yellow"]
BLOCK_SIZE = 10
CANVAS_HEIGHT = BLOCK_SIZE * MAP_SIZE[0]
CANVAS_WIDTH = BLOCK_SIZE * MAP_SIZE[1]


class Painter():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('my_window')
        # self.window.geometry('400x400')
        self.canvas = tk.Canvas(self.window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        # print(self.canvas.index())

    def draw_map(self, map):
        row = MAP_SIZE[0]
        col = MAP_SIZE[1]
        for x0 in range(0, row):
            for y0 in range(0, col):
                if map[x0, y0]:
                    self.canvas.create_rectangle(x0 * BLOCK_SIZE, y0 * BLOCK_SIZE, (x0 + 1) * BLOCK_SIZE,
                                                 (y0 + 1) * BLOCK_SIZE, fill=BLOCK_COLOR[0], outline="white", width=2)
                else:
                    self.canvas.create_rectangle(x0 * BLOCK_SIZE, y0 * BLOCK_SIZE, (x0 + 1) * BLOCK_SIZE,
                                                 (y0 + 1) * BLOCK_SIZE, fill=BLOCK_COLOR[1], outline="white", width=2)
