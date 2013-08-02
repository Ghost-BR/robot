# coding: utf-8

import unittest

from robot import robot


class RobotTestCase(unittest.TestCase):

    def test_create(self):
        r = robot.Robot()
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.pointing, 'N')
        r = robot.Robot(6, 7, 'L')
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.pointing, 'L')

    def test_posision(self):
        r = robot.Robot()
        self.assertAlmostEqual(r.pos(), (0, 0, 'N'))
        r = robot.Robot(3, 4, 'S')
        self.assertAlmostEqual(r.pos(), (3, 4, 'S'))

    def test_direction(self):
        r = robot.Robot()
        with self.assertRaises(ValueError):
            r.pointing = 'H'

    def test_turn(self):
        r = robot.Robot()
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
        r = robot.Robot()
        r.walk()
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 1)
        r.turn('R')
        r.walk()
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        r.turn('R')
        r.walk()
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 0)
        r.turn('R')
        r.walk()
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_teletransport(self):
        r = robot.Robot()
        r.teletransport(20, 10)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 10)

if __name__ == "__main__":
    unittest.main()
