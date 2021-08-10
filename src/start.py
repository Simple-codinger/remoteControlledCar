#!/usr/bin/env python3

from motor import Motor
import pygame
from time import sleep
   
axes_left = [0, 1]
axes_right = [3, 4]
axis_L = 2
axis_R = 5
check_frequency = 10
button_L1 = 4
button_L2 = 6
button_L3 = 11
button_R1 = 5
button_R2 = 7
button_R3 = 12

button_Triangle = 2
button_Circle = 1
button_X = 0
button_Rectangle = 3

button_Arrow_Up = 13
button_Arrow_Right = 16
button_Arrow_Down = 14
button_Arrow_Left = 15

button_Select = 8
button_Start = 9
button_PS = 10

def main():
    pygame.init()
    j = pygame.joystick.Joystick(0)
    j.init()
    print("Detected controller :" + j.get_name())

    # Init Motor
    motor1 = Motor(2, 3, 4, 17, 22, 27)
    motor1.stop(0)

    isRunning = True
    turn = 0.0
    isForward = False
    isBackward = False

    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(button_Rectangle) == 1:
                    motor1.stop(0)
                    isRunning = False
                    break
            if event.type == pygame.JOYAXISMOTION:
                if j.get_axis(axis_R) > -1 and not isBackward:
                    isForward = True
                    speed = j.get_axis(axis_R) + 1
                    speed = speed * 0.5
                    motor1.move(speed, turn, 0)
                elif j.get_axis(axis_R) == -1 and isForward:
                    isForward = False
                    motor1.stop(0)
                elif j.get_axis(axis_L) > -1 and not isForward:
                    isForward = False
                    isBackward = True
                    speed = j.get_axis(axis_L) + 1
                    speed = speed * 0.5
                    motor1.move(-speed, turn, 0)
                elif j.get_axis(axis_L) == -1 and isBackward:
                    isBackward = False
                    motor1.stop(0)

                turn = -(j.get_axis(axes_left[0]))
                if not isBackward and not isForward:
                    if turn != 0:
                        motor1.move(0, turn, 0)
                    else:
                        motor1.stop(0)


                

        sleep(1/check_frequency)
    j.quit()

if __name__ == "__main__":
    main()
