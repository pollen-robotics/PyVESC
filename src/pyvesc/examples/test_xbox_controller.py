#!/usr/bin/env python
# coding: utf-8
import pygame
import time
import sys
import traceback


def main():
    try:
        # Init pygame and joystick
        pygame.init()
        pygame.display.init()
        pygame.joystick.init()

        nb_joy = pygame.joystick.get_count()
        if nb_joy < 1:
            print("No controller detected.")
            sys.exit()
        print("nb joysticks: {}".format(nb_joy))
        j = pygame.joystick.Joystick(0)
        j.init()
        print(f"Using joystick: {j.get_name()}")

        while True:
            # Pump events to keep pygame state updated
            for event in pygame.event.get():
                pass

            # Left stick: axis 0 (left/right), axis 1 (up/down)
            left_x = j.get_axis(0)
            left_y = j.get_axis(1)

            # Right stick: axis 3 (left/right), axis 4 (up/down)
            right_x = j.get_axis(3)
            right_y = j.get_axis(4)

            print(
                f"Left stick  (x={left_x:.2f}, y={left_y:.2f}) | "
                f"Right stick (x={right_x:.2f}, y={right_y:.2f})"
            )

            time.sleep(0.05)

    except Exception:
        traceback.print_exc()
    finally:
        print("Exiting...")
        pygame.quit()


if __name__ == "__main__":
    main()
