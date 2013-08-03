# coding: utf-8


def limit(line):
    values = [int(value) for value in line.strip().split()]
    if len(values) != 2:
        raise ValueError('Wrong limit passed')
    return tuple(values)


def initial_position(line):
    values = [value for value in line.strip().split()]
    if len(values) != 3:
        raise ValueError('Wrong initial position passed')
    if len(values[2]) != 1 and not values[2].isalpha():
        raise ValueError('Wrong pointing position passed')
    return ((int(values[0]), int(values[1])), values[2])
