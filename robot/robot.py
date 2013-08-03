# coding: utf-8


class OutBoundError(Exception):
    '''Error when try to move robot out of limits'''


class Robot(object):

    VALID_ORIENTATION = ['N', 'L', 'S', 'O']
    MAP_ORIENTATION = {
        'N': 0,
        'L': 1,
        'S': 2,
        'O': 3,
    }
    WALK = {
        'N': (0, 1),
        'L': (1, 0),
        'S': (0, -1),
        'O': (-1, 0),
    }

    def __init__(self, pos=(0, 0), pointing='N', limit=(10, 10)):
        self.limit_x, self.limit_y = limit
        self.pos = pos
        self.pointing = pointing

    @property
    def pointing(self):
        return self._pointing

    @pointing.setter
    def pointing(self, new_pointing):
        if new_pointing not in self.VALID_ORIENTATION:
            raise ValueError('{} is not a valid value for pointing'
                             .format(new_pointing))
        self._pointing = new_pointing

    @property
    def pos(self):
        return self._x, self._y

    @pos.setter
    def pos(self, new_pos):
        x, y = new_pos

        if x < 0 or x >= self.limit_x or y < 0 or y >= self.limit_y:
            raise OutBoundError('Moving out of limits')

        self._x = x
        self._y = y

    @property
    def full_position(self):
        return self.pos, self.pointing

    def turn(self, direction):
        index = self.MAP_ORIENTATION[self.pointing]
        if direction == 'L':
            index -= 1
        elif(direction == 'R'):
            index += 1
        else:
            raise ValueError('{} is not a valid value for direction'
                             .format(direction))

        self.pointing = self.VALID_ORIENTATION[index % 4]

    def walk(self):
        x, y = self.WALK[self._pointing]
        self.pos = (self._x + x, self._y + y)

    def teletransport(self, new_pos):
        self.pos = new_pos
