from unittest import TestCase, main
from Robot_client import *


class TestRobot(TestCase):
    def test_Robot___init__(self):
        addr = None
        left_id = None
        right_id = None
        left_trim = None
        right_trim = None
        stop_at_exit = None
        self.assertEqual(Robot___init__(addr, left_id, right_id, left_trim, right_trim, stop_at_exit), None)

    def test_Robot__left_speed(self):
        speed = None
        self.assertEqual(Robot__left_speed(speed), None)

    def test_Robot__right_speed(self):
        speed = None
        self.assertEqual(Robot__right_speed(speed), None)

    def test_Robot_stop(self):
        self.assertEqual(Robot_stop(), None)

    def test_Robot_forward(self):
        speed = None
        seconds = None
        self.assertEqual(Robot_forward(speed, seconds), None)

    def test_Robot_backward(self):
        speed = None
        seconds = None
        self.assertEqual(Robot_backward(speed, seconds), None)

    def test_Robot_right(self):
        speed = None
        seconds = None
        self.assertEqual(Robot_right(speed, seconds), None)

    def test_Robot_left(self):
        speed = None
        seconds = None
        self.assertEqual(Robot_left(speed, seconds), None)

if __name__ == '__main__':
    main()
