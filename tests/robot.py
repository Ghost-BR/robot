# coding: utf-8

import unittest

from robot import robot


class RobotTestCase(unittest.TestCase):

    def test_create(self):
        r = robot.Robot()
        self.assertEqual(r.pos, (0, 0))
        self.assertEqual(r.pointing, 'N')
        r = robot.Robot((6, 7), 'L')
        self.assertEqual(r.pos, (6, 7))
        self.assertEqual(r.pointing, 'L')

    def test_posision(self):
        r = robot.Robot()
        self.assertAlmostEqual(r.full_position, ((0, 0), 'N'))
        r = robot.Robot((3, 4), 'S')
        self.assertAlmostEqual(r.full_position, ((3, 4), 'S'))

    def test_direction(self):
        r = robot.Robot()
        r.pointing = 'N'
        self.assertEqual(r.pointing, 'N')
        r.pointing = 'S'
        self.assertEqual(r.pointing, 'S')
        r.pointing = 'L'
        self.assertEqual(r.pointing, 'L')
        r.pointing = 'O'
        self.assertEqual(r.pointing, 'O')

        with self.assertRaises(ValueError):
            r.pointing = 'H'
            r.pointing = 'R'
            r.pointing = 'A'

    def test_turn(self):
        r = robot.Robot(pointing='N')
        self.assertEqual(r.pointing, 'N')
        r.turn('L')
        self.assertEqual(r.pointing, 'O')
        r.turn('L')
        self.assertEqual(r.pointing, 'S')
        r.turn('L')
        self.assertEqual(r.pointing, 'L')
        r.turn('L')
        self.assertEqual(r.pointing, 'N')
        r.turn('R')
        self.assertEqual(r.pointing, 'L')
        r.turn('R')
        self.assertEqual(r.pointing, 'S')
        r.turn('R')
        self.assertEqual(r.pointing, 'O')
        r.turn('R')
        self.assertEqual(r.pointing, 'N')

    def test_walk(self):
        r = robot.Robot(pos=(0, 0), pointing='N')
        r.walk()
        self.assertEqual(r.pos, (0, 1))
        r.turn('R')
        r.walk()
        self.assertEqual(r.pos, (1, 1))
        r.turn('R')
        r.walk()
        self.assertEqual(r.pos, (1, 0))
        r.turn('R')
        r.walk()
        self.assertEqual(r.pos, (0, 0))

    def test_teletransport(self):
        r = robot.Robot()
        r.teletransport((5, 5))
        self.assertEqual(r.pos, (5, 5))

    def test_out_of_limits(self):
        r = robot.Robot(pos=(9, 9), limit=(10, 10))
        with self.assertRaises(robot.OutBoundError):
            r.walk()
            r.teletransport((20, 10))
            robot.Robot(pos=(2, 1), limit=(2, 4))
            robot.Robot(pos=(1, 4), limit=(2, 4))
            robot.Robot(pos=(2, 4), limit=(2, 4))
            robot.Robot(pos=(3, 1), limit=(2, 4))
            robot.Robot(pos=(1, 5), limit=(2, 4))
            robot.Robot(pos=(2, 5), limit=(2, 4))


if __name__ == "__main__":
    unittest.main()
