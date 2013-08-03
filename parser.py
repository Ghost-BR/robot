# coding: utf-8
import robot


def limit(line):
    '''Parse limit of board'''
    values = [int(value) for value in line.strip().split()]
    if len(values) != 2:
        raise ValueError('Wrong limit passed')
    return tuple(values)


def initial_position(line):
    '''Parse initial position'''
    values = [value for value in line.strip().split()]
    if len(values) != 3:
        raise ValueError('Wrong initial position passed')
    orientation = values[2]
    if len(orientation) != 1 and orientation not in robot.VALID_ORIENTATION:
        raise ValueError('Wrong pointing position passed')
    return ((int(values[0]), int(values[1])), orientation)


def read_commands(line):
    '''Parse a line of commands in tubles to be passed to robot'''
    line = line.strip()
    command_list = []

    if 'T' in line:
        position = [int(value) for value in line.split()[1:]]
        if len(position) != 2:
            raise ValueError('Wrong arguments for teleport')
        command_list.append(('teleport', tuple(position)))
    else:
        for value in line:
            if value in ('L', 'R'):
                new_command = ('turn', value)
            elif value == 'M':
                new_command = ('move',)
            else:
                raise ValueError('Wrong commands to robot')
            command_list.append(new_command)
    return command_list


def parse_file(fname):
    '''Parse a file and return limit, initial, position and commands'''
    with open(fname) as fp:
        limits = limit(fp.readline())
        position = initial_position(fp.readline())
        commands = []
        for line in fp:
            commands += read_commands(line)
    return limits, position, commands
