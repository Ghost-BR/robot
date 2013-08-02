# coding: utf-8


class Robot(object):

    VALID_ORIENTATION = ['N', 'L', 'S', 'O']
    MAP_ORIENTATION = {
        'N': 0,
        'L': 1,
        'S': 2,
        'O': 3,
    }

    def __init__(self, x=0, y=0, pointing='N'):
        self.x = x
        self.y = y
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

    def pos(self):
        return (self.x, self.y, self.pointing)

    def turn(self, direction):
        if direction not in ('L', 'R'):
            raise ValueError('{} is not a valid value for direction'
                             .format(direction))
        index = self.MAP_ORIENTATION[self.pointing]
        if direction == 'L':
            index -= 1
        else:
            index += 1

        if index < 0:
            index = 3
        elif index > 3:
            index = 0

        self.pointing = self.VALID_ORIENTATION[index]

    def walk(self):
        if self._pointing == 'N':
            self.y += 1
        elif self._pointing == 'S':
            self.y -= 1
        elif self._pointing == 'L':
            self.x += 1
        elif self._pointing == 'O':
            self.x -= 1

    def teletransport(self, x, y):
        self.x = x
        self.y = y
