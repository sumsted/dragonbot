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
        robot.forward()
    elif c == 's':
        robot.backward()
    elif c == 'a':
        robot.left()
    elif c == 'd':
        robot.right()
    elif c == ' ':
        robot.stop()
    elif c == 'z':
        robot.left_rot()
    elif c == 'c':
        robot.right_rot()
    else:
        print('unknown command')

print('stop')
