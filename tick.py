import time
import logic
import ui
import threading
import tkinter as tk

FPS = 1000


class Tick(object):
    def __init__(self):
        self.logic_cycle = logic.Logic()
        self.painter = ui.Painter()
        self.logic_cycle.mode = 1
        self.thread_1 = threading.Thread(target=self.start, daemon=True)

    def start(self):
        try:
            while True:
                self.painter.canvas.delete(tk.ALL)
                self.painter.draw_map(self.logic_cycle.main_map.get())
                self.logic_cycle.main_map.set()
                time.sleep(0.5)
                self.painter.window.update()

        except KeyboardInterrupt:
            print("Game Over")

    def main_loop(self):
        self.painter.window.mainloop()
