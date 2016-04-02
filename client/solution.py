import robot


while True:
    print("'w'=forward, 's'=backward, 'a'=left, 'd'=right, ")
    print("space=stop, 'z'=rotate left, 'c'=rotate right, 'q'=quit ")
    c = input("command: ")
    print(c)
    if c == 'q':
        break
print('stop')
