# coding: utf-8

VALID_ORIENTATION = ['N', 'E', 'S', 'W']

MAP_ORIENTATION = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

MOVE = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}


class OutBoundError(Exception):
    '''Error when try to move robot out of limits'''


class CommandError(Exception):
    '''Error when try to pass a wrong command'''


class Robot(object):
    '''Robot that can move in a board'''

    def __init__(self, pos=(0, 0), pointing='N', limits=(10, 10),
                 position=None):
        '''pos tuple(x, y)
        pointing orientation
        or position tuple( tuple(x,y), orientation)
        limits possible area that robot can move
        '''
        if position is not None:
            pos = position[0]
            pointing = position[1]
        self.limit_x, self.limit_y = limits
        self.pos = pos
        self.pointing = pointing

    @property
    def pointing(self):
        return self._pointing

    @pointing.setter
    def pointing(self, new_pointing):
        if new_pointing not in VALID_ORIENTATION:
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

    def turn(self, direction):
        '''turn robot to left or right'''
        index = MAP_ORIENTATION[self.pointing]
        if direction == 'L':
            index -= 1
        elif(direction == 'R'):
            index += 1
        else:
            raise ValueError('{} is not a valid value for direction'
                             .format(direction))

        self.pointing = VALID_ORIENTATION[index % 4]

    def move(self):
        '''Robot move forward'''
        x, y = MOVE[self._pointing]
        self.pos = (self._x + x, self._y + y)

    def teleport(self, new_pos):
        '''Robot teleport to a given position'''
        self.pos = new_pos

    def from_commands(self, commands):
        '''Robot execute a list of commands'''
        for command_instruction in commands:
            command = command_instruction[0]
            if command not in ('turn', 'move', 'teleport'):
                raise CommandError('{} not a valid command'. format(command))
            action = self.__getattribute__(command)
            action(*command_instruction[1:])


if __name__ == '__main__':
    import os
    import sys

    import parser

    fname = os.path.join('input', 'example.txt')
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    limits, position, commands = parser.parse_file(fname)
    r = Robot(position=position, limits=limits)
    r.from_commands(commands)
    x, y = r.pos
    print('{0} {1} {2}'.format(x, y, r.pointing))
