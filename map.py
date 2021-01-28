import numpy as np
MAP_SIZE = (30, 30)


class Map(object):
    def __init__(self):
        self.map = np.zeros(MAP_SIZE)
        self.reset()

    def reset(self):
        self.map = np.random.randint(0, 2, MAP_SIZE)
        # self.map = np.array(exp1)
        print('reset')


    def get_neighbor_count(self, position):
        x_axis = position[0]
        y_axis = position[1]
        cube_left = max(0, x_axis - 1)
        cube_up = max(0, y_axis - 1)
        cube_right = min(MAP_SIZE[0], x_axis + 1) + 1
        cube_down = min(MAP_SIZE[1], y_axis + 1) + 1
        # neighbor_size = self.map[cube_left:cube_right,cube_up:cube_down].shape
        neighbor_count = self.map[cube_left:cube_right,cube_up:cube_down].sum() - self.map[x_axis,y_axis]
        return neighbor_count

    def set(self):
        neighbor_count_map = np.zeros(MAP_SIZE)
        for x_axis in range(0, MAP_SIZE[0]):
            for y_axis in range(0, MAP_SIZE[1]):
                neighbor_count = self.get_neighbor_count((x_axis, y_axis))
                state = self.map[x_axis,y_axis]
                if state:
                    if neighbor_count > 3:
                        state_next = 0
                    elif neighbor_count == 3 or neighbor_count == 2:
                        state_next = 1
                    else:
                        state_next = 0
                else:
                    if neighbor_count == 3:
                        state_next = 1
                    else:
                        state_next = 0
                neighbor_count_map[x_axis,y_axis] = state_next
        self.map = neighbor_count_map
        print('update')

    def get(self):
        return self.map
