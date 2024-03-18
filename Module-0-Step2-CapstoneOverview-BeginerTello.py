# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:35:40 2023

@author: sb5
"""
# Install Package for Tello drone from https://pypi.org/project/djitellopy/
#pip install djitellopy


from djitellopy import Tello
import time

def main():
    # Initialize the Tello drone
    tello = Tello('192.168.87.23')

    # Connect to the drone
    print("Connecting to drone...")
    tello.connect()
    print("Connected to drone.")

    # Check the battery level
    print(f"Current battery level: {tello.get_battery()}%")

    # Take off
    print("Taking off...")
    tello.takeoff()
    time.sleep(5)

    # Fly forward
    print("Flying forward...")
    tello.move_forward(10)
    time.sleep(5)


    # Fly forward
    print("Flying forward...")
    tello.move_up(10)

    # Fly forward
    print("Flying forward...")
    tello.flip_forward()
    tello.rotate_counter_clockwise(90)

    # Fly forward
    print("Flying forward...")
    tello.move_forward(10)
    time.sleep(5)


    # Land
    print("Landing...")
    tello.land()

if __name__ == "__main__":
    main()