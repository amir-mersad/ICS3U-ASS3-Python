#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program checks if a rectangle is a square


def main():
    # This function checks if a rectangle is a square

    # Input
    side1str = input("Please enter the length of the rectangle: ")
    side2str = input("Please enter the width of the rectangle: ")

    # Process & Output
    try:
        side1 = int(side1str)
        side2 = int(side2str)
        if side1 == side2:
            print("Your rectangle is a square!")
        elif side1 != side2:
            print("Your rectangle is not a square!")
    except Exception:
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
