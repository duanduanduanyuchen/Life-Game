import map


class Logic(object):
    def __init__(self):
        self.main_map = map.Map()
        self.mode = 0  # 0 for pause 1 for game 2 for reset

    def game_cycle(self):
        if self.mode == 1:
            self.main_map.set()
        elif self.mode == 2:
            self.main_map.reset()
            self.mode = 1
        return self.main_map.get()

