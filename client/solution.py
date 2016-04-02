import dragonbot as robot

robot.robot_debug = False

while True:
    print("\n'w'=forward, 's'=backward, 'a'=left, 'd'=right, ")
    print("space=stop, 'z'=rotate left, 'c'=rotate right, 'q'=quit ")
    c = input("command: ")
    print(c)
    if c == 'q':
        break
    elif c == 'w':
        robot.forward(1)
    elif c == 's':
        robot.backward(1)
    elif c == 'a':
        robot.left(1)
    elif c == 'd':
        robot.right(1)
    elif c == ' ':
        robot.stop(1)
    elif c == 'z':
        robot.left_rot(1)
    elif c == 'c':
        robot.right_rot(1)
    else:
        print('unknown command')

print('stop')
