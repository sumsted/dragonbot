__author__ = 'scottumsted'
import time
import Robot_client


robot_debug = True
robot_speed = 100


def pause(t=0.5, sleep=False):
    if t > 5.0:
        duration = 5.0
    elif t < .2:
        duration = .2
    else:
        duration = t
    if sleep:
        time.sleep(duration)
    return duration


def forward(duration=0.5):
    print('robot_controller, forward, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_forward(robot_speed, seconds)


def backward(duration=0.5):
    print('robot_controller, backward, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_backward(robot_speed, seconds)


def left(duration=0.5):
    print('robot_controller, left, robot_debug =', robot_debug)
    if not robot_debug:
        Robot_client.Robot__left_speed(robot_speed)
        Robot_client.Robot__right_speed(0)
        pause(duration, True)
        Robot_client.Robot_stop()


def left_rot(duration=0.5):
    print('robot_controller, left_rot, robot_debug =', robot_debug)
    if not robot_debug:
        Robot_client.Robot__left_speed(robot_speed)
        Robot_client.Robot__right_speed(-robot_speed)
        pause(duration, True)
        Robot_client.Robot_stop()


def right(duration=0.5):
    print('robot_controller, right, robot_debug =', robot_debug)
    if not robot_debug:
        Robot_client.Robot__left_speed(0)
        Robot_client.Robot__right_speed(robot_speed)
        pause(duration, True)
        Robot_client.Robot_stop()


def right_rot(duration=0.5):
    print('robot_controller, right_rot, robot_debug =', robot_debug)
    if not robot_debug:
        Robot_client.Robot__left_speed(-robot_speed)
        Robot_client.Robot__right_speed(robot_speed)
        pause(duration, True)
        Robot_client.Robot_stop()


def stop(duration=0.5):
    print('robot_controller, stop, robot_debug =', robot_debug)
    if not robot_debug:
        Robot_client.Robot_stop()
        pause(duration, True)


def distance():
    d = 0
    return d


def blink(times=5):
    pass


def volt():
    v = 0
    return v


def servo(position):
    pass


if __name__ == '__main__':
    robot_debug = False
    left(.5)
    right(1)
    forward(2)
    stop()
    backward(10)
    distance()

