# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program determines which month it is depending on the number given.


def main():
    # this functions runs the program

    # input
    integer = int(input("Enter an integer: "))

    # process
    if (integer == 1):
        print("January")
    elif (integer == 2):
        print("February")
    elif (integer == 3):
        print("March")
    elif (integer == 4):
        print("April")
    elif (integer == 5):
        print("May")
    elif (integer == 6):
        print("June")
    elif (integer == 7):
        print("July")
    elif (integer == 8):
        print("August")
    elif (integer == 9):
        print("September")
    elif (integer == 10):
        print("October")
    elif (integer == 11):
        print("November")
    elif (integer == 12):
        print("December")


if __name__ == "__main__":
    main()
