# coding: utf-8

import os
import unittest

import robot
import parser


class RobotTestCase(unittest.TestCase):

    def test_create(self):
        r = robot.Robot()
        self.assertEqual(r.pos, (0, 0))
        self.assertEqual(r.pointing, 'N')
        r = robot.Robot((6, 7), 'E')
        self.assertEqual(r.pos, (6, 7))
        self.assertEqual(r.pointing, 'E')
        r = robot.Robot(position=((6, 7), 'E'))
        self.assertEqual(r.pos, (6, 7))
        self.assertEqual(r.pointing, 'E')
        r = robot.Robot(pos=(2, 2), pointing='S', position=((6, 7), 'E'))
        self.assertEqual(r.pos, (6, 7))
        self.assertEqual(r.pointing, 'E')

    def test_posision(self):
        r = robot.Robot()
        self.assertEqual(r.pos, (0, 0))
        self.assertEqual(r.pointing, 'N')
        r = robot.Robot((3, 4), 'S')
        self.assertEqual(r.pos, (3, 4))
        self.assertEqual(r.pointing, 'S')

    def test_direction(self):
        r = robot.Robot()
        r.pointing = 'N'
        self.assertEqual(r.pointing, 'N')
        r.pointing = 'S'
        self.assertEqual(r.pointing, 'S')
        r.pointing = 'E'
        self.assertEqual(r.pointing, 'E')
        r.pointing = 'W'
        self.assertEqual(r.pointing, 'W')

        with self.assertRaises(ValueError):
            r.pointing = 'H'
            r.pointing = 'R'
            r.pointing = 'A'

    def test_turn(self):
        r = robot.Robot(pointing='N')
        self.assertEqual(r.pointing, 'N')
        r.turn('L')
        self.assertEqual(r.pointing, 'W')
        r.turn('L')
        self.assertEqual(r.pointing, 'S')
        r.turn('L')
        self.assertEqual(r.pointing, 'E')
        r.turn('L')
        self.assertEqual(r.pointing, 'N')
        r.turn('R')
        self.assertEqual(r.pointing, 'E')
        r.turn('R')
        self.assertEqual(r.pointing, 'S')
        r.turn('R')
        self.assertEqual(r.pointing, 'W')
        r.turn('R')
        self.assertEqual(r.pointing, 'N')

    def test_move(self):
        r = robot.Robot(pos=(0, 0), pointing='N')
        r.move()
        self.assertEqual(r.pos, (0, 1))
        r.turn('R')
        r.move()
        self.assertEqual(r.pos, (1, 1))
        r.turn('R')
        r.move()
        self.assertEqual(r.pos, (1, 0))
        r.turn('R')
        r.move()
        self.assertEqual(r.pos, (0, 0))

    def test_teleport(self):
        r = robot.Robot()
        r.teleport((5, 5))
        self.assertEqual(r.pos, (5, 5))

    def test_out_of_limits(self):
        r = robot.Robot(pos=(9, 9), limits=(10, 10))
        with self.assertRaises(robot.OutBoundError):
            r.move()
            r.teleport((20, 10))
            robot.Robot(pos=(2, 1), limits=(2, 4))
            robot.Robot(pos=(1, 4), limits=(2, 4))
            robot.Robot(pos=(2, 4), limits=(2, 4))
            robot.Robot(pos=(3, 1), limits=(2, 4))
            robot.Robot(pos=(1, 5), limits=(2, 4))
            robot.Robot(pos=(2, 5), limits=(2, 4))

    def test_from_command(self):
        r = robot.Robot()
        command_list = [
            ('turn', 'R'),
            ('move',),
            ('turn', 'L'),
            ('move',),
        ]
        r.from_commands(command_list)
        self.assertEqual(r.pos, (1, 1))
        self.assertEqual(r.pointing, 'N')

        command_list = [
            ('teleport', (5, 5)),
        ]
        r.from_commands(command_list)
        self.assertEqual(r.pos, (5, 5))
        self.assertEqual(r.pointing, 'N')

        self.assertRaises(robot.CommandError, r.from_commands, [('pos',)])


class ParserTestCase(unittest.TestCase):

    def test_limits(self):
        limit = parser.limit('12 15')
        self.assertEqual(limit, (12, 15))
        self.assertEqual(len(limit), 2)

        with self.assertRaises(ValueError):
            parser.limit('')
            parser.limit('12')
            parser.limit('12 13 15')
            parser.limit('RLM')

    def test_initial_position(self):
        position = parser.initial_position('10 12 N')
        self.assertEqual(position, ((10, 12), 'N'))
        with self.assertRaises(ValueError):
            parser.initial_position('')
            parser.initial_position('12')
            parser.initial_position('12 13 15')
            parser.initial_position('12 S 11')
            parser.initial_position('RLM')

    def test_commands(self):
        commands = parser.read_commands('RMLM')
        expected = [
            ('turn', 'R'),
            ('move',),
            ('turn', 'L'),
            ('move',),
        ]
        self.assertEqual(commands, expected)

        commands = parser.read_commands('T 10 20')
        expected = [
            ('teleport', (10, 20)),
        ]
        self.assertEqual(commands, expected)

        with self.assertRaises(ValueError):
            parser.read_commands('T 10 20 30')
            parser.read_commands('RT 10 20')
            parser.read_commands('MLMT')

    def test_parse_file(self):
        expected_commands = [
            ('move',),
            ('turn', 'L'),
            ('move',),
            ('turn', 'L'),
            ('move',),
            ('turn', 'R'),
            ('move',),
            ('teleport', (5, 5)),
            ('move',),
            ('turn', 'L'),
            ('turn', 'L'),
            ('move',),
        ]
        correct_file = os.path.join('input', 'correct.txt')
        wrong_limits = os.path.join('input', 'wrong_limits.txt')
        wrong_position = os.path.join('input', 'wrong_position.txt')
        wrong_commands = os.path.join('input', 'wrong_commands.txt')

        limits, position, commands = parser.parse_file(correct_file)
        self.assertEqual(limits, (20, 30))
        self.assertEqual(position, ((2, 2), 'W'))
        self.assertEqual(commands, expected_commands)

        with self.assertRaises(ValueError):
            parser.parse_file(wrong_limits)
            parser.parse_file(wrong_position)
            parser.parse_file(wrong_commands)


if __name__ == "__main__":
    unittest.main()
